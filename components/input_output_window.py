from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from UI.input_output_window_ui import Ui_InputOutputWindow


class InputOutputWindow(QWidget):
    def __init__(
        self, intput_path: str = "", output_path: str = "", selected_file: bool = False
    ):
        super().__init__()
        self._input_path = intput_path
        self._output_path = output_path

        self.ui = Ui_InputOutputWindow()
        self.ui.setupUi(self)

        self.ui.inputEdit.setText(intput_path)
        self.ui.outputEdit.setText(output_path)
        self.ui.selectFileRadioBtn.setChecked(selected_file)

        self.modify_select_btn_text(selected_file)

        self.ui.inputBtn.clicked.connect(self.selectInputBtnSolt)
        self.ui.outputBtn.clicked.connect(self.selectOutputBtnSlot)
        self.ui.selectFileRadioBtn.clicked.connect(self.modify_select_btn_text)

    @property
    def input_path(self) -> str:
        if self._input_path == "":
            QMessageBox(
                QMessageBox.Icon.Critical,
                "错误",
                "源文件路径不能为空",
                QMessageBox.StandardButton.Ok,
            ).exec()
            return ""

        return self._input_path

    @property
    def output_path(self) -> str:
        if self._output_path == "":
            QMessageBox(
                QMessageBox.Icon.Critical,
                "错误",
                "输出文件路径不能为空",
                QMessageBox.StandardButton.Ok,
            ).exec()
            return ""
        return self._output_path

    def is_selected_file(self) -> bool:
        return self.ui.selectFileRadioBtn.isChecked()

    def modify_select_btn_text(self, selected_file: bool):
        self.ui.inputEdit.clear()
        self.ui.outputEdit.clear()

        if selected_file:
            self.ui.inputBtn.setText("选择输入文件")
            self.ui.outputBtn.setText("选择输出文件")
            self.ui.inputEdit.setPlaceholderText("输入文件路径")
            self.ui.outputEdit.setPlaceholderText("输出文件路径")
        else:
            self.ui.inputBtn.setText("选择输入目录")
            self.ui.outputBtn.setText("选择输出目录")
            self.ui.inputEdit.setPlaceholderText("输入目录路径")
            self.ui.outputEdit.setPlaceholderText("输出目录路径")

    @property
    def is_selected_file(self) -> bool:
        return self._is_selected_file

    def selectInputBtnSolt(self):
        fileName = ""
        if self.ui.selectFileRadioBtn.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(
                self, "选择源文件", "", "All Files (*)"
            )
        else:
            fileName = QFileDialog.getExistingDirectory(
                self, "选择源文件夹", "./"
            )
        self.ui.inputEdit.setText(fileName)
        self._input_path = fileName

    def selectOutputBtnSlot(self):
        fileName = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "./tmp")
        self.ui.outputEdit.setText(fileName)
        self._output_path = fileName


if __name__ == "__main__":
    from PySide6.QtWidgets import (
        QApplication,
    )
    import sys

    app = QApplication(sys.argv)
    window = InputOutputWindow()
    window.show()
    sys.exit(app.exec())
