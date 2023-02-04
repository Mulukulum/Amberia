# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectEditorLyScvo.ui'
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


class ProjectEditDialog(object):
    def setupUi(self, Dialog,projectname: str):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(594, 351)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit)

        self.ToggleColorEdit=QRadioButton(Dialog)
        self.ToggleColorEdit.setText("Choose whether to Change Color of the project ")
        self.verticalLayout.addWidget(self.ToggleColorEdit)

        self.ColorEdit=QColorDialog(Dialog)
        self.ColorEdit.setWindowFlags(Qt.Widget)
        self.ColorEdit.setOptions(QColorDialog.DontUseNativeDialog|QColorDialog.NoButtons)
        self.verticalLayout.addWidget(self.ColorEdit)
        self.ColorEdit.setDisabled(True)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.lineEdit.setText(projectname)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog,):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Project Name", None))
    # retranslateUi

