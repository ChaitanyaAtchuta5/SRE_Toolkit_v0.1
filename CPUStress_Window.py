# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guikpJGSe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(260, 60, 251, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.UserInp = QLineEdit(self.formLayoutWidget)
        self.UserInp.setObjectName(u"UserInp")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.UserInp)

        self.ServerInp = QLineEdit(self.formLayoutWidget)
        self.ServerInp.setObjectName(u"ServerInp")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ServerInp)

        self.PwdInp = QLineEdit(self.formLayoutWidget)
        self.PwdInp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PwdInp.setObjectName(u"PwdInp")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.PwdInp)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 20, 161, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(340, 140, 91, 81))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WindowsRB = QRadioButton(self.verticalLayoutWidget_2)
        self.WindowsRB.setObjectName(u"WindowsRB")
        self.WindowsRB.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.WindowsRB)

        self.LinuxRB = QRadioButton(self.verticalLayoutWidget_2)
        self.LinuxRB.setObjectName(u"LinuxRB")

        self.verticalLayout_2.addWidget(self.LinuxRB)

        self.ConnectBtn = QPushButton(self.verticalLayoutWidget_2)
        self.ConnectBtn.setObjectName(u"ConnectBtn")

        self.verticalLayout_2.addWidget(self.ConnectBtn)

        self.ConnStatusTxt = QLabel(self.centralwidget)
        self.ConnStatusTxt.setObjectName(u"ConnStatusTxt")
        self.ConnStatusTxt.setGeometry(QRect(300, 219, 158, 34))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.ConnStatusTxt.setFont(font1)
        self.ConnStatusTxt.setStyleSheet(u"color: red")
        self.ConnStatusTxt.setAlignment(Qt.AlignCenter)
        self.ConnStatusTxt.setWordWrap(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 260, 91, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 260, 151, 21))
        self.label_7.setFont(font2)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(380, 270, 16, 251))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(150, 307, 71, 101))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        self.CPUper_RBGrp = QButtonGroup(self.centralwidget)
        self.CPUper25RB = QRadioButton(self.verticalLayoutWidget_3)
        self.CPUper25RB.setObjectName(u"CPUper25RB")
        
        self.verticalLayout_3.addWidget(self.CPUper25RB)
        self.CPUper_RBGrp.addButton(self.CPUper25RB)

        self.CPUper50RB = QRadioButton(self.verticalLayoutWidget_3)
        self.CPUper50RB.setObjectName(u"CPUper50RB")
        
        self.verticalLayout_3.addWidget(self.CPUper50RB)
        self.CPUper_RBGrp.addButton(self.CPUper50RB)

        self.CPUper75RB = QRadioButton(self.verticalLayoutWidget_3)
        self.CPUper75RB.setObjectName(u"CPUper75RB")

        self.verticalLayout_3.addWidget(self.CPUper75RB)
        self.CPUper_RBGrp.addButton(self.CPUper75RB)

        self.CPUper100RB = QRadioButton(self.verticalLayoutWidget_3)
        self.CPUper100RB.setObjectName(u"CPUper100RB")

        self.verticalLayout_3.addWidget(self.CPUper100RB)
        self.CPUper_RBGrp.addButton(self.CPUper100RB)

        self.DurationInp = QSpinBox(self.centralwidget)
        self.DurationInp.setObjectName(u"DurationInp")
        self.DurationInp.setGeometry(QRect(159, 445, 42, 22))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(109, 447, 47, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 450, 47, 13))
        self.CPUSExecBtn = QPushButton(self.centralwidget)
        self.CPUSExecBtn.setObjectName(u"CPUSExecBtn")
        self.CPUSExecBtn.setGeometry(QRect(150, 500, 75, 23))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(400, 300, 391, 185))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.JMBatchLblTxt = QLabel(self.gridLayoutWidget)
        self.JMBatchLblTxt.setObjectName(u"JMBatchLblTxt")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.JMBatchLblTxt.setFont(font3)

        self.gridLayout.addWidget(self.JMBatchLblTxt, 0, 0, 1, 1)

        self.JMBatchFileLocInp = QLineEdit(self.gridLayoutWidget)
        self.JMBatchFileLocInp.setObjectName(u"JMBatchFileLocInp")

        self.gridLayout.addWidget(self.JMBatchFileLocInp, 1, 0, 1, 1)

        self.JMOputFolderLocInp = QLineEdit(self.gridLayoutWidget)
        self.JMOputFolderLocInp.setObjectName(u"JMOputFolderLocInp")

        self.gridLayout.addWidget(self.JMOputFolderLocInp, 5, 0, 1, 1)

        self.JMOputFolderBrowseBtn = QPushButton(self.gridLayoutWidget)
        self.JMOputFolderBrowseBtn.setObjectName(u"JMOputFolderBrowseBtn")

        self.gridLayout.addWidget(self.JMOputFolderBrowseBtn, 5, 1, 1, 1)

        self.JMBatchFileBrowseBtn = QPushButton(self.gridLayoutWidget)
        self.JMBatchFileBrowseBtn.setObjectName(u"JMBatchFileBrowseBtn")

        self.gridLayout.addWidget(self.JMBatchFileBrowseBtn, 1, 1, 1, 1)

        self.JMScriptFileLocInp = QLineEdit(self.gridLayoutWidget)
        self.JMScriptFileLocInp.setObjectName(u"JMScriptFileLocInp")

        self.gridLayout.addWidget(self.JMScriptFileLocInp, 3, 0, 1, 1)

        self.JMScriptFileBrowseBtn = QPushButton(self.gridLayoutWidget)
        self.JMScriptFileBrowseBtn.setObjectName(u"JMScriptFileBrowseBtn")

        self.gridLayout.addWidget(self.JMScriptFileBrowseBtn, 3, 1, 1, 1)

        self.JMResLblTxt = QLabel(self.gridLayoutWidget)
        self.JMResLblTxt.setObjectName(u"JMResLblTxt")
        self.JMResLblTxt.setFont(font3)

        self.gridLayout.addWidget(self.JMResLblTxt, 4, 0, 1, 1)

        self.JMScriptLblTxt = QLabel(self.gridLayoutWidget)
        self.JMScriptLblTxt.setObjectName(u"JMScriptLblTxt")
        self.JMScriptLblTxt.setFont(font3)

        self.gridLayout.addWidget(self.JMScriptLblTxt, 2, 0, 1, 1)

        self.JMOputFileLblTxt = QLabel(self.gridLayoutWidget)
        self.JMOputFileLblTxt.setObjectName(u"JMOputFileLblTxt")
        self.JMOputFileLblTxt.setFont(font3)

        self.gridLayout.addWidget(self.JMOputFileLblTxt, 6, 0, 1, 1)

        self.JMOputFileInp = QLineEdit(self.gridLayoutWidget)
        self.JMOputFileInp.setObjectName(u"JMOputFileInp")

        self.gridLayout.addWidget(self.JMOputFileInp, 7, 0, 1, 1)

        self.JMOputFormatTxt = QLabel(self.gridLayoutWidget)
        self.JMOputFormatTxt.setObjectName(u"JMOputFormatTxt")
        self.JMOputFormatTxt.setFont(font3)

        self.gridLayout.addWidget(self.JMOputFormatTxt, 7, 1, 1, 1)

        self.JMExecBtn = QPushButton(self.centralwidget)
        self.JMExecBtn.setObjectName(u"JMExecBtn")
        self.JMExecBtn.setGeometry(QRect(560, 500, 75, 23))
        self.CPUSExecStatusTxt = QLabel(self.centralwidget)
        self.CPUSExecStatusTxt.setObjectName(u"CPUSExecStatusTxt")
        self.CPUSExecStatusTxt.setGeometry(QRect(110, 530, 158, 34))
        self.CPUSExecStatusTxt.setFont(font1)
        self.CPUSExecStatusTxt.setStyleSheet(u"color: blue")
        self.CPUSExecStatusTxt.setAlignment(Qt.AlignCenter)
        self.CPUSExecStatusTxt.setWordWrap(True)
        self.JMExecStatusTxt = QLabel(self.centralwidget)
        self.JMExecStatusTxt.setObjectName(u"JMExecStatusTxt")
        self.JMExecStatusTxt.setGeometry(QRect(510, 530, 158, 34))
        self.JMExecStatusTxt.setFont(font1)
        self.JMExecStatusTxt.setStyleSheet(u"color: blue")
        self.JMExecStatusTxt.setAlignment(Qt.AlignCenter)
        self.JMExecStatusTxt.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server Address", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SRE ToolKit v0.1", None))
        self.WindowsRB.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.LinuxRB.setText(QCoreApplication.translate("MainWindow", u"Linux", None))
        self.ConnectBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ConnStatusTxt.setText(QCoreApplication.translate("MainWindow", u"Not Connected", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CPU Stress", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Jmeter Execution", None))
        self.CPUper25RB.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.CPUper50RB.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.CPUper75RB.setText(QCoreApplication.translate("MainWindow", u"75%", None))
        self.CPUper100RB.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.CPUSExecBtn.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.JMBatchLblTxt.setText(QCoreApplication.translate("MainWindow", u"Select Jmeter batch file path ", None))
        self.JMOputFolderBrowseBtn.setText(QCoreApplication.translate("MainWindow", u"Choose Location", None))
        self.JMBatchFileBrowseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.JMScriptFileBrowseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.JMResLblTxt.setText(QCoreApplication.translate("MainWindow", u"Select Jmeter results path ", None))
        self.JMScriptLblTxt.setText(QCoreApplication.translate("MainWindow", u"Select Jmeter script file ", None))
        self.JMOputFileLblTxt.setText(QCoreApplication.translate("MainWindow", u"Output Filename ", None))
        self.JMOputFormatTxt.setText(QCoreApplication.translate("MainWindow", u".jtl", None))
        self.JMExecBtn.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.CPUSExecStatusTxt.setText("")
        self.JMExecStatusTxt.setText("")
    # retranslateUi

