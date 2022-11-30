# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TasksTodayWindowQyZfBP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TaskTodayUI(object):
    def setupUi(self, Form):

        '''
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(792, 536)
        '''
        
        Form.setMinimumSize(QSize(550, 500))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame = QFrame(self.frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.gridLayout = QGridLayout(self.horizontalFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SortNameButton = QPushButton(self.horizontalFrame)
        self.SortNameButton.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.SortNameButton, 0, 0, 1, 1)

        self.SortPriorityButton = QPushButton(self.horizontalFrame)
        self.SortPriorityButton.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.SortPriorityButton, 0, 1, 1, 1)

        self.SortProjectButton = QPushButton(self.horizontalFrame)
        self.SortProjectButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.SortProjectButton, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        
        self.ScrollAreaContentsForTaskWidgets = QWidget()
        self.ScrollAreaContentsForTaskWidgets.setObjectName(u"ScrollAreaForTaskWidgets")
        self.ScrollAreaContentsForTaskWidgets.setGeometry(QRect(0, 0, 752, 465))
        self.VLayoutForTaskWidgets = QVBoxLayout(self.ScrollAreaContentsForTaskWidgets)
        self.VLayoutForTaskWidgets.setObjectName(u"VLayoutForTaskWidgets")
        
        self.scrollArea.setWidget(self.ScrollAreaContentsForTaskWidgets)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.SortNameButton.setText(QCoreApplication.translate("Form", u"Sort by Name", None))
        self.SortPriorityButton.setText(QCoreApplication.translate("Form", u"Sort by Priority", None))
        self.SortProjectButton.setText(QCoreApplication.translate("Form", u"Sort by Project", None))
    # retranslateUi

