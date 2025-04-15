from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    def __init__(self, config: str):
        super().__init__()
        self.config = config
        self._parse_config()

    def _parse_config(self):
        raise NotImplementedError
