from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from UI.ReplaceChapter_ui import Ui_ReplaceChapter
from components.base_page import BasePage
class ReplaceChapter(BasePage):
    def __init__(self,config):
        super().__init__(config)
        self.ui = Ui_ReplaceChapter()
        self.ui.setupUi(self)
        

        self.ui.srcBtn.clicked.connect(self.selectSrcFile)
        self.ui.outputBtn.clicked.connect(self.selectOutputFile)
        
    def _parse_config(self):
        pass
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