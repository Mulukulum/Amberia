# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskEditVDzjSt.ui'
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
        Form.resize(684, 602)
        Form.setStyleSheet(u"background : #2c2825;")
        '''
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TaskDueLabel = QLabel(self.frame)
        self.TaskDueLabel.setObjectName(u"TaskDueLabel")
        self.TaskDueLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.TaskDueLabel, 3, 0, 1, 1)

        self.PriorityLabel = QLabel(self.frame)
        self.PriorityLabel.setObjectName(u"PriorityLabel")
        self.PriorityLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.PriorityLabel, 4, 0, 1, 1)

        self.EnableDueDateButton=QRadioButton(self.frame)
        self.EnableDueDateButton.setText("Choose whether to enable setting a due date")
        self.gridLayout_2.addWidget(self.EnableDueDateButton,2,0,1,1)

        self.PriorityLevelEdit = QDoubleSpinBox(self.frame)
        self.PriorityLevelEdit.setObjectName(u"PriorityLevelEdit")
        self.PriorityLevelEdit.setMinimumSize(QSize(0, 50))
        self.PriorityLevelEdit.setWrapping(True)
        self.PriorityLevelEdit.setDecimals(0)
        self.PriorityLevelEdit.setMinimum(1.000000000000000)
        self.PriorityLevelEdit.setMaximum(10.000000000000000)

        self.gridLayout_2.addWidget(self.PriorityLevelEdit, 4, 1, 1, 1)

        self.TaskTitleEdit = QLineEdit(self.frame)
        self.TaskTitleEdit.setObjectName(u"TaskTitleEdit")
        self.TaskTitleEdit.setMinimumSize(QSize(0, 50))

        self.gridLayout_2.addWidget(self.TaskTitleEdit, 0, 0, 1, 2)

        self.TaskDescEdit = QTextEdit(self.frame)
        self.TaskDescEdit.setObjectName(u"TaskDescEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TaskDescEdit.sizePolicy().hasHeightForWidth())
        self.TaskDescEdit.setSizePolicy(sizePolicy)
        self.TaskDescEdit.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout_2.addWidget(self.TaskDescEdit, 1, 0, 1, 2)

        self.DueDateEdit = QDateTimeEdit(self.frame)
        self.DueDateEdit.setObjectName(u"DueDateEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DueDateEdit.sizePolicy().hasHeightForWidth())
        self.DueDateEdit.setSizePolicy(sizePolicy1)
        self.DueDateEdit.setMinimumSize(QSize(100, 50))
        self.DueDateEdit.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.DueDateEdit, 3, 1, 1, 1)

        self.CancelButton = QPushButton(self.frame)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.clicked.connect(lambda: Form.reject())
        self.gridLayout_2.addWidget(self.CancelButton, 5, 0, 1, 1)
        
        self.SubmitButton = QPushButton(self.frame)
        self.SubmitButton.setObjectName(u"SubmitButton")
        self.SubmitButton.clicked.connect(lambda: Form.accept())
        self.gridLayout_2.addWidget(self.SubmitButton, 5, 1, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        self.DueDateEdit.setDisabled(True)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TaskDueLabel.setText(QCoreApplication.translate("Form", u"Task Due Date:", None))
        self.PriorityLabel.setText(QCoreApplication.translate("Form", u"Task Priority Level:", None))
        self.PriorityLevelEdit.setPrefix("")
        self.TaskTitleEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Task Title Here", None))
        self.TaskDescEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Describe Your Task or Add Notes Here", None))
        self.CancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.SubmitButton.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

