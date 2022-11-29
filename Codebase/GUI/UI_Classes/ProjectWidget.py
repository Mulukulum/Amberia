# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectWidgetsSTyyW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ProjectWidget(object):
    def setupUi(self, MainWidgetFrame):
        '''
        if MainWidgetFrame.objectName():
            MainWidgetFrame.setObjectName(u"MainWidgetFrame")
        MainWidgetFrame.resize(886, 500)
        '''
        MainWidgetFrame.setMinimumSize(QSize(300, 300))
        self.gridLayout = QGridLayout(MainWidgetFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.ProjectInfoFrame = QFrame(MainWidgetFrame)
        self.ProjectInfoFrame.setObjectName(u"ProjectInfoFrame")
        self.ProjectInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.ProjectInfoFrame.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout = QHBoxLayout(self.ProjectInfoFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.ProjectName = QLabel(self.ProjectInfoFrame)
        self.ProjectName.setObjectName(u"ProjectName")

        self.horizontalLayout.addWidget(self.ProjectName)

        self.AddSection = QPushButton(self.ProjectInfoFrame)
        self.AddSection.setObjectName(u"AddSection")

        self.horizontalLayout.addWidget(self.AddSection)

        self.EditDetails = QPushButton(self.ProjectInfoFrame)
        self.EditDetails.setObjectName(u"EditDetails")

        self.horizontalLayout.addWidget(self.EditDetails)

        self.DeleteProject = QPushButton(self.ProjectInfoFrame)
        self.DeleteProject.setObjectName(u"DeleteProject")

        self.horizontalLayout.addWidget(self.DeleteProject)


        self.gridLayout.addWidget(self.ProjectInfoFrame, 0, 0, 1, 1)

        self.ProjectSectionsScrollArea = QScrollArea(MainWidgetFrame)
        self.ProjectSectionsScrollArea.setObjectName(u"ProjectSectionsScrollArea")
        self.ProjectSectionsScrollArea.setWidgetResizable(True)

        self.SectionWidgetArea = QWidget()
        self.SectionWidgetArea.setObjectName(u"SectionWidgetArea")
        self.SectionWidgetArea.setGeometry(QRect(0, 0, 866, 409))

        self.LayoutToAddSections = QVBoxLayout(self.SectionWidgetArea)
        self.LayoutToAddSections.setObjectName(u"LayoutToAddSections")
        self.ProjectSectionsScrollArea.setWidget(self.SectionWidgetArea)

        self.gridLayout.addWidget(self.ProjectSectionsScrollArea, 1, 0, 1, 1)


        self.retranslateUi(MainWidgetFrame)

        QMetaObject.connectSlotsByName(MainWidgetFrame)
    # setupUi

    def retranslateUi(self, MainWidgetFrame):
        MainWidgetFrame.setWindowTitle(QCoreApplication.translate("MainWidgetFrame", u"Form", None))
        self.ProjectName.setText(QCoreApplication.translate("MainWidgetFrame", u"ProjectName", None))
        self.AddSection.setText(QCoreApplication.translate("MainWidgetFrame", u"Add Section", None))
        self.EditDetails.setText(QCoreApplication.translate("MainWidgetFrame", u"Edit Details", None))
        self.DeleteProject.setText(QCoreApplication.translate("MainWidgetFrame", u"Delete Project", None))
    # retranslateUi

