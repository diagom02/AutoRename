# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoRenamefmszuh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 205)
        MainWindow.setMinimumSize(QSize(550, 205))
        MainWindow.setMaximumSize(QSize(550, 205))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.default_folder = QLineEdit(self.centralwidget)
        self.default_folder.setObjectName(u"default_folder")

        self.horizontalLayout_2.addWidget(self.default_folder)

        self.browse_button = QToolButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout_2.addWidget(self.browse_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fansubs_2 = QLabel(self.centralwidget)
        self.fansubs_2.setObjectName(u"fansubs_2")

        self.verticalLayout.addWidget(self.fansubs_2)

        self.fansubs = QLineEdit(self.centralwidget)
        self.fansubs.setObjectName(u"fansubs")

        self.verticalLayout.addWidget(self.fansubs)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.anime_name_2 = QLabel(self.centralwidget)
        self.anime_name_2.setObjectName(u"anime_name_2")

        self.verticalLayout_2.addWidget(self.anime_name_2)

        self.anime_name = QLineEdit(self.centralwidget)
        self.anime_name.setObjectName(u"anime_name")

        self.verticalLayout_2.addWidget(self.anime_name)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Formato_2 = QLabel(self.centralwidget)
        self.Formato_2.setObjectName(u"Formato_2")

        self.verticalLayout_3.addWidget(self.Formato_2)

        self.Formato = QLineEdit(self.centralwidget)
        self.Formato.setObjectName(u"Formato")

        self.verticalLayout_3.addWidget(self.Formato)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ext_name_2 = QLabel(self.centralwidget)
        self.ext_name_2.setObjectName(u"ext_name_2")

        self.verticalLayout_4.addWidget(self.ext_name_2)

        self.ext_name = QLineEdit(self.centralwidget)
        self.ext_name.setObjectName(u"ext_name")

        self.verticalLayout_4.addWidget(self.ext_name)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.final_result = QLineEdit(self.centralwidget)
        self.final_result.setObjectName(u"final_result")
        self.final_result.setEnabled(False)

        self.verticalLayout_5.addWidget(self.final_result)

        self.rename_button = QPushButton(self.centralwidget)
        self.rename_button.setObjectName(u"rename_button")
        self.rename_button.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(12)
        self.rename_button.setFont(font)

        self.verticalLayout_5.addWidget(self.rename_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Directorio fuente:", None))
        self.default_folder.setText("")
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.fansubs_2.setText(QCoreApplication.translate("MainWindow", u"FanSubs:", None))
        self.anime_name_2.setText(QCoreApplication.translate("MainWindow", u"Nombre del Anime:", None))
        self.Formato_2.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.ext_name_2.setText(QCoreApplication.translate("MainWindow", u"Extensi\u00f3n:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resultado final:", None))
        self.rename_button.setText(QCoreApplication.translate("MainWindow", u"Renombrar archivos", None))
    # retranslateUi

