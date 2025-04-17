from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QTextEdit,
    QProgressBar,
    QSplitter,
)
from PySide6.QtCore import Qt
from components.base_page import BasePage
from UI.export_sql_ui import Ui_ExportSql
from components.input_output_window import InputOutputWindow
from dataclasses import dataclass, field


@dataclass
class RegEx:
    regex: str = ""
    topic: str = ""


@dataclass
class ChapterRegEx:
    name_reg_ex: list[RegEx] = field(default_factory=list)


class ExportSql(BasePage):
    def __init__(self, config):
        super().__init__(config)

        self.export_window = QWidget()
        self.export_window_ui = Ui_ExportSql()
        self.export_window_ui.setupUi(self.export_window)

        self.input_output = InputOutputWindow()

        layout = QVBoxLayout(self)
        layout.addWidget(self.input_output)
        layout.addWidget(self.export_window)

        self.export_window_ui.treeWidget.setHeaderHidden(True)
        chapter_reg_ex_tree_item = QTreeWidgetItem("Regex")
        self.export_window_ui.treeWidget.addTopLevelItem(chapter_reg_ex_tree_item)
        for reg in self._chapter_reg_ex.name_reg_ex:
            chapter_reg_ex_tree_item.addChild(QTreeWidgetItem([reg.regex, reg.topic]))

    def _parse_config(self):
        self._chapter_reg_ex = ChapterRegEx()
        for item in self.config.data.get("chapter_reg_ex", []):
            reg = item.get("reg_ex", "")
            topic = item.get("topic", "")
            self._chapter_reg_ex.name_reg_ex.append(RegEx(regex=reg, topic=topic))
