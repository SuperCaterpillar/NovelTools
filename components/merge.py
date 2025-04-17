from PySide6.QtWidgets import (
    QWidget,
    QFileDialog,
    QMessageBox,
)
from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt


from UI.merge_ui import Ui_Merge
from functions.megre_work import MergeWorker
from components.base_page import BasePage
from dataclasses import dataclass, field


@dataclass
class MergeRegEx:
    regex: str = ""
    topic: str = ""


@dataclass
class MergePageConfig:
    name_reg_ex: list[MergeRegEx] = field(default_factory=list)


class Merge(BasePage):

    def __init__(self, config: str):
        super().__init__(config)
        self.ui = Ui_Merge()
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

        # config_path = "config/config.json"
        # config = ConfigParser.parse(config_path)

        for reg_ex in self.merge_page_config.name_reg_ex:
            self.ui.regEXCombo.addItem(reg_ex.regex)
            # self.ui.regEXCombo.setToolTip()

    def _parse_config(self):
        self.merge_page_config = MergePageConfig()
        for item in self.config.data.get("merge_reg_ex", []):
            reg = item.get("reg_ex", "")
            topic = item.get("topic", "")
            self.merge_page_config.name_reg_ex.append(MergeRegEx(regex=reg, topic=topic))

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
        fileName = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "./tmp")
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

        self.ui.textBrowser.clear()

        # if self.worker_thread and self.worker_thread.isRunning():
        #     self.show_error("线程已在运行中")
        #     return
        self.worker_thread = QThread(self)
        self.worker = MergeWorker(output_dir, input_dir, fileRegEx, is_single_file)
        

        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.fileTotal.connect(lambda total: self.ui.progressBar.setMaximum(total))
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.worker.status.connect(self.ui.textBrowser.append)
        self.worker.error.connect(self.show_error)

        self.worker_thread.finished.connect(self.worker_thread.deleteLater)

        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_merge)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.init()
        self.worker_thread.start()

    def show_error(self, error_msg):
        QMessageBox(
            QMessageBox.Icon.Critical, "错误", error_msg, QMessageBox.StandardButton.Ok
        ).exec()
