import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QListWidget, QStackedWidget,QSplitter
)

from pathlib import Path
from PySide6.QtCore import Qt

from functions.config import ConfigParser

# 动态加载页面类
def load_page_class(module_path, class_name):
    try:
        print(f"加载页面: {module_path}   {class_name}")
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    except Exception as e:
        print(f"加载页面失败: {module_path}.{class_name} - {str(e)}")
        return None
    


        
class ToolManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动态工具管理界面")
        self.setGeometry(100, 100, 800, 600)

        # 加载配置文件
        config_path = Path(__file__).parent / "config/config.json"
        config = ConfigParser.parse(config_path)

        # 创建主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(8)  # 设置分隔条宽度
      #   self.splitter.setChildrenCollapsible(False)  # 禁止折叠子部件

        # 左侧功能列表
        self.function_list = QListWidget()
      #   self.function_list.setIconSize(QSize(32, 32))
      #   self.function_list.setFixedWidth(180)
        self.splitter.addWidget(self.function_list)

        # 右侧页面容器
        self.pages_container = QStackedWidget()
        self.splitter.addWidget(self.pages_container)

        # 动态生成页面
        self.pages = []
        for page_config in config.pages:
            module_path = page_config.stack_setting.Module
            class_name = page_config.stack_setting.Page
            page_class = load_page_class(module_path, class_name)
            
            if page_class:
                page = page_class()
                self.pages_container.addWidget(page)
                self.function_list.addItem(
                  #   QIcon(page_config.get("icon", "")),
                    page_config.fun_setting.Name
                )
        
        self.function_list.currentRowChanged.connect(
            lambda row: self.pages_container.setCurrentIndex(row)
        )
        self.splitter.setStretchFactor(0, 3)  # 设置左侧部件的拉伸比例
        self.splitter.setStretchFactor(1, 9)  # 设置左侧部件的拉伸比例
        # 设置主窗口的中心部件
        main_widget.setLayout(QHBoxLayout())
        main_widget.layout().addWidget(self.splitter)
        

if __name__ == "__main__":
    
    sys.path.append(str(Path(__file__).parent.parent))  
    app = QApplication(sys.argv)
    window = ToolManager()
    window.show()
    sys.exit(app.exec())