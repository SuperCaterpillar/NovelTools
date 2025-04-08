from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background: #f0f0f0;")
        layout = QVBoxLayout(self)
        label = QLabel("这是功能2页面")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)