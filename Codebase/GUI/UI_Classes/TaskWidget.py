# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskWidgetQXXTOu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TaskWidgetUI(object):
    def setupUi(self, Form):
        '''
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(874, 329)
        '''
        Form.setMinimumSize(QSize(550, 200))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.DeleteTaskButton = QPushButton(Form)
        self.DeleteTaskButton.setObjectName(u"DeleteTaskButton")

        self.gridLayout.addWidget(self.DeleteTaskButton, 2, 5, 1, 2)

        self.DaysLeftLabel = QLabel(Form)
        self.DaysLeftLabel.setObjectName(u"DaysLeftLabel")

        self.gridLayout.addWidget(self.DaysLeftLabel, 0, 3, 1, 1)

        self.TaskDescription = QTextBrowser(Form)
        self.TaskDescription.setObjectName(u"textBrowser")
        self.TaskDescription.setReadOnly(False)

        self.gridLayout.addWidget(self.TaskDescription, 1, 0, 1, 7)

        self.DaysLeftDisplay = QLCDNumber(Form)
        self.DaysLeftDisplay.setObjectName(u"DaysLeftDisplay")
        self.DaysLeftDisplay.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.DaysLeftDisplay.setDigitCount(5)
        self.DaysLeftDisplay.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.DaysLeftDisplay, 0, 4, 1, 1)

        self.PriorityLabel = QLabel(Form)
        self.PriorityLabel.setObjectName(u"PriorityLabel")

        self.gridLayout.addWidget(self.PriorityLabel, 0, 5, 1, 1)

        self.PriorityLevelDisplay = QLCDNumber(Form)
        self.PriorityLevelDisplay.setObjectName(u"PriorityLevelDisplay")
        self.PriorityLevelDisplay.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.PriorityLevelDisplay.setSmallDecimalPoint(False)
        self.PriorityLevelDisplay.setDigitCount(2)
        self.PriorityLevelDisplay.setProperty("intValue", 10)

        self.gridLayout.addWidget(self.PriorityLevelDisplay, 0, 6, 1, 1)


        #self.TaskFrame = QFrame(Form)
        #self.TaskFrame.setObjectName(u"TaskFrame")
        #self.TaskFrame.setFrameShape(QFrame.StyledPanel)
        #self.TaskFrame.setFrameShadow(QFrame.Raised)
        #self.horizontalLayout_2 = QHBoxLayout(self.TaskFrame)
        #self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        #self.gridLayout.addWidget(self.TaskFrame, 3, 0, 1, 7)

        self.TaskTitle_label = QLabel(Form)
        self.TaskTitle_label.setObjectName(u"TaskTitle_label")

        self.gridLayout.addWidget(self.TaskTitle_label, 0, 0, 1, 3)

        self.EditTaskButton = QPushButton(Form)
        self.EditTaskButton.setObjectName(u"EditTaskButton")

        self.gridLayout.addWidget(self.EditTaskButton, 2, 0, 1, 2)

        self.ReminderBox = QCheckBox(Form)
        self.ReminderBox.setObjectName(u"ReminderBox")
        font = QFont()
        font.setPointSize(10)
        self.ReminderBox.setFont(font)
        self.ReminderBox.setCursor(QCursor(Qt.ArrowCursor))
        self.ReminderBox.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.ReminderBox, 2, 2, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DeleteTaskButton.setText(QCoreApplication.translate("Form", u"Delete Task", None))
        self.DaysLeftLabel.setText(QCoreApplication.translate("Form", u"Days Left:", None))
        self.TaskDescription.setMarkdown("")
        self.TaskDescription.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.TaskDescription.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Description Here", None))
        self.PriorityLabel.setText(QCoreApplication.translate("Form", u"Priority Level :", None))
        self.TaskTitle_label.setText(QCoreApplication.translate("Form", u"TaskName", None))
        self.EditTaskButton.setText(QCoreApplication.translate("Form", u"Edit Task", None))
        self.ReminderBox.setText(QCoreApplication.translate("Form", u"Remind Me", None))
    # retranslateUi

