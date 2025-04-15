# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Merge(object):
    def setupUi(self, Merge):
        if not Merge.objectName():
            Merge.setObjectName(u"Merge")
        Merge.resize(931, 697)
        self.verticalLayout_3 = QVBoxLayout(Merge)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.srcBtn = QPushButton(Merge)
        self.srcBtn.setObjectName(u"srcBtn")

        self.gridLayout.addWidget(self.srcBtn, 2, 1, 1, 1)

        self.label = QLabel(Merge)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.outputEdit = QLineEdit(Merge)
        self.outputEdit.setObjectName(u"outputEdit")

        self.gridLayout.addWidget(self.outputEdit, 3, 0, 1, 1)

        self.fileSeletBtn = QRadioButton(Merge)
        self.fileSeletBtn.setObjectName(u"fileSeletBtn")

        self.gridLayout.addWidget(self.fileSeletBtn, 4, 0, 1, 1)

        self.outputBtn = QPushButton(Merge)
        self.outputBtn.setObjectName(u"outputBtn")

        self.gridLayout.addWidget(self.outputBtn, 3, 1, 1, 1)

        self.srcEdit = QLineEdit(Merge)
        self.srcEdit.setObjectName(u"srcEdit")

        self.gridLayout.addWidget(self.srcEdit, 2, 0, 1, 1)

        self.regEXCombo = QComboBox(Merge)
        self.regEXCombo.setObjectName(u"regEXCombo")

        self.gridLayout.addWidget(self.regEXCombo, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(Merge)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.putAwayBtn = QPushButton(Merge)
        self.putAwayBtn.setObjectName(u"putAwayBtn")

        self.horizontalLayout.addWidget(self.putAwayBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(Merge)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(Merge)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Merge)

        QMetaObject.connectSlotsByName(Merge)
    # setupUi

    def retranslateUi(self, Merge):
        Merge.setWindowTitle(QCoreApplication.translate("Merge", u"Form", None))
        self.srcBtn.setText(QCoreApplication.translate("Merge", u"\u6e90\u6587\u4ef6\u6216\u76ee\u5f55", None))
        self.label.setText(QCoreApplication.translate("Merge", u"\u6b63\u5219\u8868\u8fbe\u5f0f", None))
        self.outputEdit.setPlaceholderText(QCoreApplication.translate("Merge", u"./", None))
        self.fileSeletBtn.setText(QCoreApplication.translate("Merge", u"\u9009\u62e9\u6587\u4ef6", None))
        self.outputBtn.setText(QCoreApplication.translate("Merge", u"\u8f93\u51fa\u6587\u4ef6", None))
        self.srcEdit.setText("")
        self.srcEdit.setPlaceholderText(QCoreApplication.translate("Merge", u"./", None))
        self.putAwayBtn.setText(QCoreApplication.translate("Merge", u"\u6536\u8d77", None))
    # retranslateUi

