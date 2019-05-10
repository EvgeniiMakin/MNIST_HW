import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import second
import design  # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import *
import cv2
from keras.models import load_model
import numpy as np
model = load_model('my_model.h5')

class ExampleApp(QtWidgets.QMainWindow, design.Ui_Program):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.scene = QtWidgets.QGraphicsScene()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.File.clicked.connect(self.operation)  # Выполнить функцию browse_folder
        self.Exit.clicked.connect(QtWidgets.qApp.quit)
        self.Paint.clicked.connect(self.painting)
        self.drawing = False
        self.dialogs = list()
        self.model = model

    def operation(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.scene.clear()
        self.textBrowser.clear()
        pixMap = QPixmap(fname)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(QRectF(0, 0, pixMap.width(), pixMap.height()), Qt.KeepAspectRatio)
        self.scene.update()
        label_result = self.calculate_digit(fname)
        self.textBrowser.append(label_result)
        
    def painting(self):
        dialog = Second(self)
        self.dialogs.append(dialog)
        dialog.show()
        
    def calculate_digit(self, fname):
        img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
        width = 28
        height = 28
        resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        if (int(gray[0][0])+int(gray[27][0])+int(gray[0][27])+int(gray[27][27])) < 128*4:
            sample_test = gray/255
        else:
            sample_test = ~gray/255
        sample_test = sample_test.reshape(-1,28,28,1)
        results = self.model.predict(sample_test)
        result = np.argmax(results,axis = 1)[0]
        if fname:
            return 'Ответ: это цифра {}'.format(result)
        else:
            return ''
    def get_answer_from_paiting(self, fname):
        self.scene.clear()
        self.textBrowser.clear()
        pixMap = QPixmap(fname)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(QRectF(0, 0, pixMap.width(), pixMap.height()), Qt.KeepAspectRatio)
        self.scene.update()
        label_result = self.calculate_digit(fname)
        self.textBrowser.append(label_result)

class Second(QtWidgets.QMainWindow, second.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.drawing = True
        self.OK.clicked.connect(self.exit_and_send_image)
        self.lastPoint = QPoint()
        self.image = QPixmap("white.jpg")
        self.setGeometry(510, 80, 800, 800)
        self.resize(self.image.width(), self.image.height())
        self.show()        
        
    def exit_and_send_image(self):
        self.image.save('temp_painting.png')
        self.hide()
        self.parent.get_answer_from_paiting(os.path.abspath("temp_painting.png"))
        
    def paintEvent(self, event):
        if self.drawing:
            painter = QPainter(self)
            painter.drawPixmap(self.rect(), self.image)
            
             
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 25, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton and self.drawing:
            self.drawing = False
            
            

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
