# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '位置识别5_6.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
import cv2
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QMainWindow, QGraphicsPixmapItem, QGraphicsView
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import os
import sys
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 480, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 480, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 480, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 350, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 350, 54, 12))
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 40, 431, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 380, 191, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(440, 380, 191, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.original_pic)
        self.pushButton_2.clicked.connect(self.capture_rec)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gesture Recognition"))
        self.pushButton.setText(_translate("MainWindow", "截取"))
        self.pushButton_2.setText(_translate("MainWindow", "识别"))
        self.pushButton_3.setText(_translate("MainWindow", "关闭"))
        self.label.setText(_translate("MainWindow", "偏转角度"))
        self.label_2.setText(_translate("MainWindow", "中心坐标"))


class PicShow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(PicShow, self).__init__(parent)
        #  self.pushButton.clicked.connect(pic_show.original_pic())
        self.setupUi(self)
        # self.path = 'C://Users/dell/Desktop/test.jpg'
        # self.pic = cv2.imread(self.path, 0)
        # self.w, self.h = self.pic.shape[0:2]
        # self.original_pic()



    def original_pic(self):
        path = 'C://Users/dell/Desktop/test.jpg'
        pic = cv2.imread(path, 0)
        w, h = pic.shape[0:2]
        pic1 = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)  # 转换通道
        frame = QImage(pic1, h, w, h * 3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)




    def capture_rec(self):
        path = 'C://Users/dell/Desktop/test.jpg'
        pic = cv2.imread(path, 0)
        w, h = pic.shape[0:2]  # 读取
        # pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)  # 转换通道
        contours, hierarchy = cv2.findContours(pic, 2, 2)
        # 寻找轮廓
        for cnt in contours:
            center_point = cv2.minAreaRect(cnt)[0]
            # 中心点坐标
            width, height = cv2.minAreaRect(cnt)[1]
            # 轮廓宽度和高度
            if width * height > 225:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                # 获取最小外接矩形的4个顶点
                box = np.int0(box)
                if 0 not in box.ravel():
                    for i in range(4):
                        cv2.line(pic, tuple(box[i]), tuple(box[(i + 1) % 4]), 1)
                        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)  # 转换通道
                    angle = str(round((cv2.minAreaRect(cnt)[2]), 3))
                    x_f = round((center_point[0]), 3)
                    y_f = round((center_point[1]), 3)
                    center_point_t = (x_f, y_f)
                    center_point_s = str(center_point_t)
        frame = QImage(pic, h, w, h * 3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)
        self.print_1(angle)
        self.print_2(center_point_s)

    def print_1(self, text):
        self.textBrowser.append(text)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def print_2(self, text):
        self.textBrowser_2.append(text)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser_2.textCursor()
        self.textBrowser_2.moveCursor(self.cursot.End)
def main():

    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    app = QApplication(sys.argv)
    pic = PicShow()
    pic.show()
    app.exec_()


if __name__ == '__main__':

    main()
