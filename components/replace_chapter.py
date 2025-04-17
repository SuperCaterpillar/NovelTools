from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from UI.ReplaceChapter_ui import Ui_ReplaceChapter
from components.base_page import BasePage
from dataclasses import dataclass, field
@dataclass
class ReplaceRegEx:
    regex: str = ""
    topic: str = ""


@dataclass
class ReplacePageConfig:
    replace_reg_ex: list[ReplaceRegEx] = field(default_factory=list)


class ReplaceChapter(BasePage):
    def __init__(self,config):
        super().__init__(config)
        self.ui = Ui_ReplaceChapter()
        self.ui.setupUi(self)
        

        self.ui.srcBtn.clicked.connect(self.selectSrcFile)
        self.ui.outputBtn.clicked.connect(self.selectOutputFile)
        
    def _parse_config(self):
        self.replace_page_config = ReplacePageConfig()
        for item in self.config.data.get("replace_reg_ex", []):
            reg = item.get("reg_ex", "")
            topic = item.get("topic", "")
            self.replace_page_config.replace_reg_ex.append(ReplaceRegEx(regex=reg, topic=topic))

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