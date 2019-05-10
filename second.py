# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowIcon(QIcon('nn.png'))
        MainWindow.resize(800, 800)
        
        
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setStyleSheet("background-color:#18BDFF; border-radius: 5px;");
        self.OK.setIcon(QIcon("ok.png"))
        self.OK.setIconSize(QSize(40, 40))  
        self.OK.setGeometry(QtCore.QRect(375, 820, 150, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OK.setFont(font)
        self.OK.setAutoFillBackground(True)
        self.OK.setObjectName("OK")
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
                                              
        
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drawing digits"))
        self.OK.setText(_translate("MainWindow", "   OK"))

