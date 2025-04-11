from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from UI.ReplaceChapter_ui import Ui_ReplaceChapter

class ReplaceChapter(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReplaceChapter()
        self.ui.setupUi(self)
        