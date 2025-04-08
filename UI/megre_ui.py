# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'megre.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Megre(object):
    def setupUi(self, Megre):
        if not Megre.objectName():
            Megre.setObjectName(u"Megre")
        Megre.resize(931, 697)
        self.verticalLayout_3 = QVBoxLayout(Megre)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.outputBtn = QPushButton(Megre)
        self.outputBtn.setObjectName(u"outputBtn")

        self.gridLayout.addWidget(self.outputBtn, 2, 1, 1, 1)

        self.srcEdit = QLineEdit(Megre)
        self.srcEdit.setObjectName(u"srcEdit")

        self.gridLayout.addWidget(self.srcEdit, 1, 0, 1, 1)

        self.label = QLabel(Megre)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.srcBtn = QPushButton(Megre)
        self.srcBtn.setObjectName(u"srcBtn")

        self.gridLayout.addWidget(self.srcBtn, 1, 1, 1, 1)

        self.regExEdit = QLineEdit(Megre)
        self.regExEdit.setObjectName(u"regExEdit")

        self.gridLayout.addWidget(self.regExEdit, 0, 0, 1, 1)

        self.outputEdit = QLineEdit(Megre)
        self.outputEdit.setObjectName(u"outputEdit")

        self.gridLayout.addWidget(self.outputEdit, 2, 0, 1, 1)

        self.fileSeletBtn = QRadioButton(Megre)
        self.fileSeletBtn.setObjectName(u"fileSeletBtn")

        self.gridLayout.addWidget(self.fileSeletBtn, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(Megre)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.putAwayBtn = QPushButton(Megre)
        self.putAwayBtn.setObjectName(u"putAwayBtn")

        self.horizontalLayout.addWidget(self.putAwayBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(Megre)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.buttonBox = QDialogButtonBox(Megre)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Megre)

        QMetaObject.connectSlotsByName(Megre)
    # setupUi

    def retranslateUi(self, Megre):
        Megre.setWindowTitle(QCoreApplication.translate("Megre", u"Form", None))
        self.outputBtn.setText(QCoreApplication.translate("Megre", u"\u8f93\u51fa\u6587\u4ef6", None))
        self.srcEdit.setText("")
        self.srcEdit.setPlaceholderText(QCoreApplication.translate("Megre", u"./", None))
        self.label.setText(QCoreApplication.translate("Megre", u"\u6b63\u5219\u8868\u8fbe\u5f0f", None))
        self.srcBtn.setText(QCoreApplication.translate("Megre", u"\u6e90\u6587\u4ef6\u6216\u76ee\u5f55", None))
        self.outputEdit.setPlaceholderText(QCoreApplication.translate("Megre", u"./", None))
        self.fileSeletBtn.setText(QCoreApplication.translate("Megre", u"\u9009\u62e9\u6587\u4ef6", None))
        self.putAwayBtn.setText(QCoreApplication.translate("Megre", u"\u6536\u8d77", None))
    # retranslateUi

