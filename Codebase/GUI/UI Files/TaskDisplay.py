# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDisplayVamfrf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):

        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TaskName = QLabel(Form)
        self.TaskName.setObjectName(u"TaskName")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        self.TaskName.setFont(font)
        self.TaskName.setLayoutDirection(Qt.LeftToRight)
        self.TaskName.setStyleSheet(u"color : rgb(236, 236, 236);")
        self.TaskName.setScaledContents(False)
        self.TaskName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.TaskName, 0, 0, 1, 3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: rgb(0, 0, 0)")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.lcdNumber, 2, 1, 1, 1)

        self.TaskCompleteButton = QPushButton(Form)
        self.TaskCompleteButton.setObjectName(u"TaskCompleteButton")
        self.TaskCompleteButton.setStyleSheet(u"background: #fdcb52;\n"
"")

        self.gridLayout.addWidget(self.TaskCompleteButton, 2, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(Form)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"background: rgb(255, 255, 255)")

        self.gridLayout.addWidget(self.lcdNumber_2, 3, 1, 1, 1)

        self.TaskDeleteButton = QPushButton(Form)
        self.TaskDeleteButton.setObjectName(u"TaskDeleteButton")
        self.TaskDeleteButton.setStyleSheet(u"background: #fdcb52;\n"
"")

        self.gridLayout.addWidget(self.TaskDeleteButton, 3, 2, 1, 1)

        self.BackButton = QPushButton(Form)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setStyleSheet(u"background: rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.BackButton, 4, 0, 1, 1)

        '''
        self.TaskEditButton = QPushButton(Form)
        self.TaskEditButton.setObjectName(u"TaskEditButton")
        self.TaskEditButton.setStyleSheet(u"background: #fdcb52;")
        

        self.gridLayout.addWidget(self.TaskEditButton, 4, 2, 1, 1)
        '''

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TaskName.setText(QCoreApplication.translate("Form", u"TaskName", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Display Description alongside the selected labels here</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Priority Level:", None))
        self.TaskCompleteButton.setText(QCoreApplication.translate("Form", u"Complete Task", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Days Left:</p></body></html>", None))
        self.TaskDeleteButton.setText(QCoreApplication.translate("Form", u"Delete Task", None))
        self.BackButton.setText(QCoreApplication.translate("Form", u"Back", None))
        # self.TaskEditButton.setText(QCoreApplication.translate("Form", u"Edit Task", None))
    # retranslateUi

