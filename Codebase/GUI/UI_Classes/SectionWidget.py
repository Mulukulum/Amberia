# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SectionWidgeteghSEA.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ParentProjectFrame(object):
    def setupUi(self, ParentProjectFrame):
        if ParentProjectFrame.objectName():
            ParentProjectFrame.setObjectName(u"ParentProjectFrame")
        ParentProjectFrame.resize(864, 300)
        ParentProjectFrame.setMinimumSize(QSize(500, 300))
        self.gridLayout = QGridLayout(ParentProjectFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SectionMenu = QHBoxLayout()
        self.SectionMenu.setObjectName(u"SectionMenu")
        self.TaskAddButton = QPushButton(ParentProjectFrame)
        self.TaskAddButton.setObjectName(u"TaskAddButton")

        self.SectionMenu.addWidget(self.TaskAddButton)

        self.SectionDeleteButton = QPushButton(ParentProjectFrame)
        self.SectionDeleteButton.setObjectName(u"SectionDeleteButton")

        self.SectionMenu.addWidget(self.SectionDeleteButton)


        self.gridLayout.addLayout(self.SectionMenu, 0, 0, 1, 1)

        self.TaskScrollArea = QScrollArea(ParentProjectFrame)
        self.TaskScrollArea.setObjectName(u"TaskScrollArea")
        self.TaskScrollArea.setWidgetResizable(True)
        self.TasksContents = QWidget()
        self.TasksContents.setObjectName(u"TasksContents")
        self.TasksContents.setGeometry(QRect(0, 0, 844, 249))
        self.verticalLayout = QVBoxLayout(self.TasksContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TaskScrollArea.setWidget(self.TasksContents)

        self.gridLayout.addWidget(self.TaskScrollArea, 1, 0, 1, 1)


        self.retranslateUi(ParentProjectFrame)

        QMetaObject.connectSlotsByName(ParentProjectFrame)
    # setupUi

    def retranslateUi(self, ParentProjectFrame):
        ParentProjectFrame.setWindowTitle(QCoreApplication.translate("ParentProjectFrame", u"Form", None))
        self.TaskAddButton.setText(QCoreApplication.translate("ParentProjectFrame", u"Add Task", None))
        self.SectionDeleteButton.setText(QCoreApplication.translate("ParentProjectFrame", u"Delete Section", None))
    # retranslateUi

