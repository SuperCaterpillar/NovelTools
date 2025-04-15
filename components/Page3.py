from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from components.base_page import BasePage
class Page3(BasePage):
    def __init__(self, config):
        super().__init__(config)
        self.setStyleSheet("background: #f0f0f0;")
        layout = QVBoxLayout(self)
        label = QLabel("这是功能3页面")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
    def _parse_config(self):
        pass