# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_output_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_InputOutputWindow(object):
    def setupUi(self, InputOutputWindow):
        if not InputOutputWindow.objectName():
            InputOutputWindow.setObjectName(u"InputOutputWindow")
        InputOutputWindow.resize(745, 83)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InputOutputWindow.sizePolicy().hasHeightForWidth())
        InputOutputWindow.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(InputOutputWindow)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputEdit = QLineEdit(InputOutputWindow)
        self.inputEdit.setObjectName(u"inputEdit")

        self.horizontalLayout.addWidget(self.inputEdit)

        self.inputBtn = QPushButton(InputOutputWindow)
        self.inputBtn.setObjectName(u"inputBtn")

        self.horizontalLayout.addWidget(self.inputBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.outputEdit = QLineEdit(InputOutputWindow)
        self.outputEdit.setObjectName(u"outputEdit")

        self.horizontalLayout_2.addWidget(self.outputEdit)

        self.outputBtn = QPushButton(InputOutputWindow)
        self.outputBtn.setObjectName(u"outputBtn")

        self.horizontalLayout_2.addWidget(self.outputBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.selectFileRadioBtn = QRadioButton(InputOutputWindow)
        self.selectFileRadioBtn.setObjectName(u"selectFileRadioBtn")

        self.verticalLayout.addWidget(self.selectFileRadioBtn)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(InputOutputWindow)

        QMetaObject.connectSlotsByName(InputOutputWindow)
    # setupUi

    def retranslateUi(self, InputOutputWindow):
        InputOutputWindow.setWindowTitle(QCoreApplication.translate("InputOutputWindow", u"Form", None))
        self.inputBtn.setText(QCoreApplication.translate("InputOutputWindow", u"\u9009\u62e9\u8f93\u5165", None))
        self.outputBtn.setText(QCoreApplication.translate("InputOutputWindow", u"\u9009\u62e9\u8f93\u51fa", None))
        self.selectFileRadioBtn.setText(QCoreApplication.translate("InputOutputWindow", u"\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

