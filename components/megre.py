from PySide6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QDialogButtonBox,
    QHBoxLayout,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt
from UI.megre_ui import Ui_Megre
import os
import re
import sys
from collections import defaultdict
from functions.config import ConfigParser
from pathlib import Path
from functions.megre_work import MergeWorker


class Megre(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Megre()
        self.ui.setupUi(self)

        sizePolichy = self.ui.textBrowser.sizePolicy()
        sizePolichy.setRetainSizeWhenHidden(True)

        self.ui.textBrowser.setSizePolicy(sizePolichy)

        self.ui.srcBtn.clicked.connect(self.selectSrcFile)
        self.ui.outputBtn.clicked.connect(self.selectOutputFile)
        self.ui.fileSeletBtn.toggled.connect(self.fileSelectToggled)
        self.ui.buttonBox.accepted.connect(self.start)
        self.ui.buttonBox.rejected.connect(self.cancel_merge)

        self.worker_thread = None

        config_path = "config/config.json"
        config = ConfigParser.parse(config_path)

        for reg_ex in config.novel_config.name_reg_ex:
            self.ui.regEXCombo.addItem(reg_ex.regex)
            # self.ui.regEXCombo.setToolTip()

        
    def fileSelectToggled(self, flag):
        if self.ui.fileSeletBtn.isChecked():
            self.ui.regEXCombo.setEnabled(True)
        else:
            self.ui.regEXCombo.setEnabled(True)

    def selectSrcFile(self):
        if self.ui.fileSeletBtn.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(
                self, "选择源文件", "", "All Files (*)"
            )
        else:
            fileName = QFileDialog.getExistingDirectory(self, "选择源文件夹", "./")
        self.ui.srcEdit.setText(fileName)

    def selectOutputFile(self):
        fileName = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "./")
        self.ui.outputEdit.setText(fileName)

    def cancel_merge(self):
        if self.worker and self.worker_thread.isRunning():
            self.worker.Cannelled()
            self.worker_thread.requestInterruption()
            self.ui.textBrowser.append("已发送取消请求...")

    def start(self):
        input_dir = self.ui.srcEdit.text()
        output_dir = self.ui.outputEdit.text()
        fileRegEx = self.ui.regEXCombo.currentText()
        is_single_file = self.ui.fileSeletBtn.isChecked()
        if input_dir == "":
            QMessageBox(
                QMessageBox.Icon.Critical,
                "错误",
                "请选择源文件夹",
                QMessageBox.StandardButton.Ok,
            ).exec()
            return
        if output_dir == "":
            output_dir = self.ui.outputEdit.placeholderText()
            self.ui.textBrowser.append(
                f"未选择输出文件夹，使用默认输出文件夹：{output_dir}"
            )

        # if self.worker_thread and self.worker_thread.isRunning():
        #     self.show_error("线程已在运行中")
        #     return
        self.worker_thread = QThread(self)
        self.worker = MergeWorker(output_dir, input_dir, fileRegEx, is_single_file)
        self.worker.init()

        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.worker.status.connect(self.ui.textBrowser.append)
        self.worker.error.connect(self.show_error)

        self.worker_thread.finished.connect(self.worker_thread.deleteLater)


        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_merge)
        self.worker.finished.connect(self.worker_thread.quit)
        
        self.worker_thread.start()

    def show_error(self, error_msg):
        QMessageBox(
            QMessageBox.Icon.Critical, "错误", error_msg, QMessageBox.StandardButton.Ok
        ).exec()
