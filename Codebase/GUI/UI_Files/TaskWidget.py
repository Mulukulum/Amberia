# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskWidgetNJyCZs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Task(object):
    def setupUi(self, Form):
        '''
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(874, 289)
        Form.setMinimumSize(QSize(550, 200))
        '''
        
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber, 0, 4, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 1)

        self.lcdNumber_2 = QLCDNumber(Form)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setProperty("intValue", 10)

        self.gridLayout.addWidget(self.lcdNumber_2, 0, 6, 1, 1)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 7)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 5, 1, 2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 834, 69))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.frame, 3, 0, 1, 7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Complete ", None))
        self.label.setText(QCoreApplication.translate("Form", u"TaskName", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Days Left:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Priority Level :", None))
        self.textBrowser.setMarkdown("")
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Description Here", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Add Labels", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Edit Task", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Delete Task", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Labels: ", None))
    # retranslateUi

