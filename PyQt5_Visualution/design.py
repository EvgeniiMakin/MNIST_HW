# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Program(object):
    def setupUi(self, Program):
        Program.setObjectName("Program")
        Program.setWindowIcon(QIcon('data/nn.png'))
        Program.resize(916, 674)
        self.centralwidget = QtWidgets.QWidget(Program)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 140, 441, 391))
        self.graphicsView.setObjectName("graphicsView")
        
        
        self.File = QtWidgets.QPushButton(self.centralwidget)
        self.File.setStyleSheet("color:white; background-color:#18BDFF; border-radius: 5px; font: 11pt \"Segoe UI Semibold\";");
        self.File.setIcon(QIcon("data/open.png"))
        self.File.setIconSize(QSize(48, 48))  
        self.File.setGeometry(QtCore.QRect(30, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.File.setFont(font)
        self.File.setAutoFillBackground(True)
        self.File.setObjectName("File")
        
        
        self.Paint = QtWidgets.QPushButton(self.centralwidget)
        self.Paint.setAutoFillBackground(True)
        self.Paint.setStyleSheet("color:white; background-color:#18BDFF; border-radius: 5px; font: 11pt \"Segoe UI Semibold\";");
        self.Paint.setIcon(QIcon("data/paint.png"))
        self.Paint.setIconSize(QSize(48, 48))  
        self.Paint.setGeometry(QtCore.QRect(320, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Paint.setFont(font)
        self.Paint.setObjectName("Paint")
        
        
   
       
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setAutoFillBackground(True)
        self.Exit.setStyleSheet("color:white; background-color:#18BDFF; border-radius: 5px; font: 11pt \"Segoe UI Semibold\";");
        self.Exit.setIcon(QIcon("data/exit.png"))
        self.Exit.setIconSize(QSize(48, 48))  
        self.Exit.setGeometry(QtCore.QRect(610, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        
        
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 570, 256, 50))
        self.textBrowser.setStyleSheet("color:white; background-color:#18BDFF; border-radius: 5px; font: 16pt \"Segoe UI Light\";")
        self.textBrowser.setObjectName("textBrowser")
        
        
        Program.setCentralWidget(self.centralwidget)

        self.retranslateUi(Program)
        QtCore.QMetaObject.connectSlotsByName(Program)

    def retranslateUi(self, Program):
        _translate = QtCore.QCoreApplication.translate
        Program.setWindowTitle(_translate("Program", "Handwritten Number Recognition Program"))
        self.File.setText(_translate("Program", "Выберите файл"))
        self.Exit.setText(_translate("Program", "      Выход"))
        self.Paint.setText(_translate("Program", " Нарисовать цифру"))
        self.textBrowser.setText(_translate("Program", "     Тут будет ответ"))
        

