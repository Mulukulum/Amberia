# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskEditOmWVSU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TaskEditUI(object):
    def setupUi(self, Form):
        '''
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setStyleSheet(u"background : #2c2825;")
        '''
        Form.resize(582, 557)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BackButton_2 = QPushButton(Form)
        self.BackButton_2.setObjectName(u"BackButton_2")
        #self.BackButton_2.setStyleSheet(u"background: rgb(255, 85, 0)")
        self.BackButton_2.clicked.connect(lambda: Form.accept())

        self.gridLayout.addWidget(self.BackButton_2, 5, 2, 1, 1)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        #self.spinBox.setStyleSheet(u"background: rgb(255,255,255)")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)

        self.gridLayout.addWidget(self.spinBox, 3, 2, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(560, 105))
        #self.textEdit.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        #self.label.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        #self.label_2.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        #self.dateTimeEdit.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.dateTimeEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateTimeEdit, 4, 1, 1, 2)

        self.BackButton = QPushButton(Form)
        self.BackButton.setObjectName(u"BackButton")
        #self.BackButton.setStyleSheet(u"background: rgb(255, 85, 0)")
        self.BackButton.clicked.connect(lambda: Form.reject())

        self.gridLayout.addWidget(self.BackButton, 5, 0, 1, 1)

        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        #self.textEdit_2.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 3)

        #self.textEdit_3 = QTextEdit(Form)
        #self.textEdit_3.setObjectName(u"textEdit_3")
        #self.textEdit_3.setStyleSheet(u"background: rgb(255, 255, 255)")

        #self.gridLayout.addWidget(self.textEdit_3, 2, 0, 1, 3)

        self.label.raise_()
        self.textEdit.raise_()
       # self.textEdit_3.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BackButton_2.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Existing Task name</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Priority Level:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Date and Time:</p></body></html>", None))
        self.BackButton.setText(QCoreApplication.translate("Form", u"Back", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Existing Description</span></p></body></html>", None))
       # self.textEdit_3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Existing Labels</span></p></body></html>", None))
    # retranslateUi

