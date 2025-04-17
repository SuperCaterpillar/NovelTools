# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_sql.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ExportSql(object):
    def setupUi(self, ExportSql):
        if not ExportSql.objectName():
            ExportSql.setObjectName(u"ExportSql")
        ExportSql.resize(901, 462)
        self.verticalLayout = QVBoxLayout(ExportSql)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(ExportSql)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.pushButton = QPushButton(ExportSql)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(ExportSql)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.treeWidget = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.splitter.addWidget(self.treeWidget)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.splitter.addWidget(self.textEdit)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.testBtn = QPushButton(ExportSql)
        self.testBtn.setObjectName(u"testBtn")

        self.horizontalLayout_2.addWidget(self.testBtn)

        self.okBtn = QPushButton(ExportSql)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)

        self.CancelBtn = QPushButton(ExportSql)
        self.CancelBtn.setObjectName(u"CancelBtn")

        self.horizontalLayout_2.addWidget(self.CancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ExportSql)

        QMetaObject.connectSlotsByName(ExportSql)
    # setupUi

    def retranslateUi(self, ExportSql):
        ExportSql.setWindowTitle(QCoreApplication.translate("ExportSql", u"Form", None))
        self.progressBar.setFormat(QCoreApplication.translate("ExportSql", u"%p%", None))
        self.pushButton.setText(QCoreApplication.translate("ExportSql", u"\u6536\u8d77", None))
        self.testBtn.setText(QCoreApplication.translate("ExportSql", u"\u6d4b\u8bd5", None))
        self.okBtn.setText(QCoreApplication.translate("ExportSql", u"\u786e\u5b9a", None))
        self.CancelBtn.setText(QCoreApplication.translate("ExportSql", u"\u53d6\u6d88", None))
    # retranslateUi

