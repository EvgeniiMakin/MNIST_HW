# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Program(object):
    def setupUi(self, Program):
        Program.setObjectName("Program")
        Program.setWindowIcon(QIcon('nn.png'))
        Program.resize(916, 674)
        self.centralwidget = QtWidgets.QWidget(Program)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 140, 441, 391))
        self.graphicsView.setObjectName("graphicsView")
        
        
        self.File = QtWidgets.QPushButton(self.centralwidget)
        self.File.setStyleSheet("background-color:#18BDFF; border-radius: 5px;");
        self.File.setIcon(QIcon("open.png"))
        self.File.setIconSize(QSize(48, 48))  
        self.File.setGeometry(QtCore.QRect(30, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.File.setFont(font)
        self.File.setAutoFillBackground(True)
        self.File.setObjectName("File")
        
        
        self.Paint = QtWidgets.QPushButton(self.centralwidget)
        self.Paint.setAutoFillBackground(True)
        self.Paint.setStyleSheet("background-color:#18BDFF; border-radius: 5px;");
        self.Paint.setIcon(QIcon("paint.png"))
        self.Paint.setIconSize(QSize(48, 48))  
        self.Paint.setGeometry(QtCore.QRect(320, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Paint.setFont(font)
        self.Paint.setObjectName("Paint")
        
        
   
       
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setAutoFillBackground(True)
        self.Exit.setStyleSheet("background-color:#18BDFF; border-radius: 5px;");
        self.Exit.setIcon(QIcon("exit.png"))
        self.Exit.setIconSize(QSize(48, 48))  
        self.Exit.setGeometry(QtCore.QRect(610, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        
        
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 570, 256, 61))
        self.textBrowser.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        
        
        Program.setCentralWidget(self.centralwidget)

        self.retranslateUi(Program)
        QtCore.QMetaObject.connectSlotsByName(Program)

    def retranslateUi(self, Program):
        _translate = QtCore.QCoreApplication.translate
        Program.setWindowTitle(_translate("Program", "Handwritten Number Recognition Program"))
        self.File.setText(_translate("Program", "Выберете файл"))
        self.Exit.setText(_translate("Program", "      Выход"))
        self.Paint.setText(_translate("Program", " Нарисовать цифру"))

        

