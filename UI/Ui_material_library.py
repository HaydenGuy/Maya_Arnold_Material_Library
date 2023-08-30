# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'material_library.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_material_window(object):
    def setupUi(self, material_window):
        if not material_window.objectName():
            material_window.setObjectName(u"material_window")
        material_window.resize(549, 226)
        material_window.setMinimumSize(QSize(236, 153))
        self.centralwidget = QWidget(material_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 531, 162))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.swatch_layout = QHBoxLayout()
        self.swatch_layout.setObjectName(u"swatch_layout")

        self.horizontalLayout.addLayout(self.swatch_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        material_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(material_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 23))
        material_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(material_window)
        self.statusbar.setObjectName(u"statusbar")
        material_window.setStatusBar(self.statusbar)

        self.retranslateUi(material_window)

        QMetaObject.connectSlotsByName(material_window)
    # setupUi

    def retranslateUi(self, material_window):
        material_window.setWindowTitle(QCoreApplication.translate("material_window", u"Material Library", None))
    # retranslateUi

