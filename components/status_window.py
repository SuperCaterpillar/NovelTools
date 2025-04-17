from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from UI.input_output_window_ui import Ui_InputOutputWindow


class InputOutputWindow(QWidget):
    def __init__(self):
        super().__init__(parent)
        self.ui = Ui_InputOutputWindow()