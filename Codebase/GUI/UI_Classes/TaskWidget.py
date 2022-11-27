# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskWidgetdYZwMI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TaskWidget(object):
    def setupUi(self, Form):

        '''
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(874, 289)
        Form.setMinimumSize(QSize(550, 200))
        '''

        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CompleteTaskButton = QPushButton(Form)
        self.CompleteTaskButton.setObjectName(u"CompleteTaskButton")

        self.gridLayout.addWidget(self.CompleteTaskButton, 0, 0, 1, 1)

        self.TaskTitle_label = QLabel(Form)
        self.TaskTitle_label.setObjectName(u"TaskTitle_label")

        self.gridLayout.addWidget(self.TaskTitle_label, 0, 1, 1, 2)

        self.DaysLeftLabel = QLabel(Form)
        self.DaysLeftLabel.setObjectName(u"DaysLeftLabel")

        self.gridLayout.addWidget(self.DaysLeftLabel, 0, 3, 1, 1)

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

        self.TaskDescription = QTextBrowser(Form)
        self.TaskDescription.setObjectName(u"TaskDescription")

        self.gridLayout.addWidget(self.TaskDescription, 1, 0, 1, 7)

        self.AddLabelsButton = QPushButton(Form)
        self.AddLabelsButton.setObjectName(u"AddLabelsButton")

        self.gridLayout.addWidget(self.AddLabelsButton, 2, 0, 1, 2)

        self.EditTaskButton = QPushButton(Form)
        self.EditTaskButton.setObjectName(u"EditTaskButton")

        self.gridLayout.addWidget(self.EditTaskButton, 2, 2, 1, 1)

        self.DeleteTaskButton = QPushButton(Form)
        self.DeleteTaskButton.setObjectName(u"DeleteTaskButton")

        self.gridLayout.addWidget(self.DeleteTaskButton, 2, 5, 1, 2)

        self.TaskFrame = QFrame(Form)
        self.TaskFrame.setObjectName(u"TaskFrame")
        self.TaskFrame.setFrameShape(QFrame.StyledPanel)
        self.TaskFrame.setFrameShadow(QFrame.Raised)
        self.LabelsHBoxLayout = QHBoxLayout(self.TaskFrame)
        self.LabelsHBoxLayout.setObjectName(u"LabelsHBoxLayout")
        self.LabelsScroller = QScrollArea(self.TaskFrame)
        self.LabelsScroller.setObjectName(u"LabelsScroller")
        font = QFont()
        font.setPointSize(12)
        self.LabelsScroller.setFont(font)
        self.LabelsScroller.setWidgetResizable(True)
        self.LabelsViewScrollContents = QWidget()
        self.LabelsViewScrollContents.setObjectName(u"LabelsViewScrollContents")
        self.LabelsViewScrollContents.setGeometry(QRect(0, 0, 834, 69))
        self.horizontalLayout = QHBoxLayout(self.LabelsViewScrollContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Labels_Title = QLabel(self.LabelsViewScrollContents)
        self.Labels_Title.setObjectName(u"Labels_Title")

        self.horizontalLayout.addWidget(self.Labels_Title)

        self.LabelsScroller.setWidget(self.LabelsViewScrollContents)

        self.LabelsHBoxLayout.addWidget(self.LabelsScroller)


        self.gridLayout.addWidget(self.TaskFrame, 3, 0, 1, 7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.CompleteTaskButton.setText(QCoreApplication.translate("Form", u"Complete ", None))
        self.TaskTitle_label.setText(QCoreApplication.translate("Form", u"TaskName", None))
        self.DaysLeftLabel.setText(QCoreApplication.translate("Form", u"Days Left:", None))
        self.PriorityLabel.setText(QCoreApplication.translate("Form", u"Priority Level :", None))
        self.TaskDescription.setMarkdown("")
        self.TaskDescription.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.TaskDescription.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Description Here", None))
        self.AddLabelsButton.setText(QCoreApplication.translate("Form", u"Add Labels", None))
        self.EditTaskButton.setText(QCoreApplication.translate("Form", u"Edit Task", None))
        self.DeleteTaskButton.setText(QCoreApplication.translate("Form", u"Delete Task", None))
        self.Labels_Title.setText(QCoreApplication.translate("Form", u"Labels: ", None))
    # retranslateUi

