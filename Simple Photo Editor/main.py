from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import resources, sys, cv2, numpy as np
import os
from small import Ui_Dialog
noImage = ""
image = ""
b = ""


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1440, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/caditor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/images/flowerbg.jfif);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 250, 1190, 650))
        self.frame.setStyleSheet("background-image: url(:/images/galacticbg.jpg);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(40, 137, 500, 375))
        self.label_1.setStyleSheet("background-image: url(:/images/whitebg.jpg);")
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(650, 137, 500, 375))
        self.label_2.setStyleSheet("background-image: url(:/images/whitebg.jpg);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_original = QtWidgets.QLabel(self.frame)
        self.label_original.setGeometry(QtCore.QRect(0, 0, 590, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setWeight(9)
        self.label_original.setFont(font)
        self.label_original.setStyleSheet("color:rgb(255, 255, 255);\n"
                                          "background-color: rgb(2, 18, 44);\n"
                                          "font: 75 20pt \"Calibri\";")
        self.label_original.setAlignment(QtCore.Qt.AlignCenter)
        self.label_original.setObjectName("label_original")
        self.label_processed = QtWidgets.QLabel(self.frame)
        self.label_processed.setGeometry(QtCore.QRect(590, 0, 600, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_processed.setFont(font)
        self.label_processed.setStyleSheet("color:rgb(255, 255, 255);\n"
                                           "background-color: rgb(2, 18, 44);\n"
                                           "font: 75 20pt \"Calibri\";")
        self.label_processed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_processed.setObjectName("label_processed")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(595, 40, 1, 610))
        self.line.setStyleSheet("Color:rgb(170, 170, 0)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.label_2.raise_()
        self.label_1.raise_()
        self.label_original.raise_()
        self.line.raise_()
        self.label_processed.raise_()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1190, 900, 250, 74))
        self.pushButton.setStyleSheet("font: 75 18pt \"Tahoma\";\n""background-image: url(:/images/khaki.jpg);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(30, 30, 200, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/caditor.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1190, 250))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 20, 750, 210))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"background-image: url(:/images/bluebg.jpg);")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_resize = QtWidgets.QWidget()
        self.tab_resize.setObjectName("tab_resize")
        self.tabWidget_2.addTab(self.tab_resize, "")
        self.label_scale = QtWidgets.QLabel(self.tab_resize)
        self.label_scale.setGeometry(QtCore.QRect(90, 30, 220, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_scale.setFont(font)
        self.label_scale.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_scale.setObjectName("label_scale")
        self.widthSlider = QtWidgets.QSlider(self.tab_resize)
        self.widthSlider.setGeometry(QtCore.QRect(340, 30, 211, 22))
        self.widthSlider.setMinimum(1)
        self.widthSlider.setMaximum(20)
        self.widthSlider.setSingleStep(1)
        self.widthSlider.setProperty("value", 10)
        self.widthSlider.setSliderPosition(10)
        self.widthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.widthSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.widthSlider.setObjectName("widthSlider")
        self.heightSlider = QtWidgets.QSlider(self.tab_resize)
        self.heightSlider.setGeometry(QtCore.QRect(340, 80, 211, 22))
        self.heightSlider.setMinimum(1)
        self.heightSlider.setMaximum(20)
        self.heightSlider.setSingleStep(1)
        self.heightSlider.setProperty("value", 10)
        self.heightSlider.setSliderPosition(10)
        self.heightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.heightSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.heightSlider.setObjectName("heightSlider")
        self.tab_rotate = QtWidgets.QWidget()
        self.tab_rotate.setObjectName("tab_rotate")
        self.b_rotateLeft = QtWidgets.QPushButton(self.tab_rotate)
        self.b_rotateLeft.setGeometry(QtCore.QRect(110, 15, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_rotateLeft.setFont(font)
        self.b_rotateLeft.setObjectName("b_rotateLeft")
        self.b_rotateRight = QtWidgets.QPushButton(self.tab_rotate)
        self.b_rotateRight.setGeometry(QtCore.QRect(290, 15, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_rotateRight.setFont(font)
        self.b_rotateRight.setObjectName("b_rotateRight")
        self.b_rotate180 = QtWidgets.QPushButton(self.tab_rotate)
        self.b_rotate180.setGeometry(QtCore.QRect(470, 15, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_rotate180.setFont(font)
        self.b_rotate180.setObjectName("b_rotate180")
        self.b_flipVertical = QtWidgets.QPushButton(self.tab_rotate)
        self.b_flipVertical.setGeometry(QtCore.QRect(90, 80, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_flipVertical.setFont(font)
        self.b_flipVertical.setObjectName("b_flipVertical")
        self.b_flipHori = QtWidgets.QPushButton(self.tab_rotate)
        self.b_flipHori.setGeometry(QtCore.QRect(490, 80, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.b_flipHori.setFont(font)
        self.b_flipHori.setObjectName("b_flipHori")
        self.rotateSlider = QtWidgets.QSlider(self.tab_rotate)
        self.rotateSlider.setGeometry(QtCore.QRect(250, 90, 221, 31))
        self.rotateSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rotateSlider.setMinimum(-360)
        self.rotateSlider.setMaximum(360)
        self.rotateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rotateSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.rotateSlider.setTickInterval(1)
        self.rotateSlider.setObjectName("rotateSlider")
        self.sliderLabel = QtWidgets.QLabel(self.tab_rotate)
        self.sliderLabel.setGeometry(QtCore.QRect(333, 130, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(13)
        self.sliderLabel.setFont(font)
        self.sliderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sliderLabel.setObjectName("sliderLabel")
        self.tabWidget_2.addTab(self.tab_rotate, "")
        self.tab_perspective = QtWidgets.QWidget()
        self.tab_perspective.setObjectName("tab_perspective")
        self.label_persp = QtWidgets.QLabel(self.tab_perspective)
        self.label_persp.setGeometry(QtCore.QRect(10, 30, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_persp.setFont(font)
        self.label_persp.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_persp.setObjectName("label_persp")
        self.label_persp_2 = QtWidgets.QLabel(self.tab_perspective)
        self.label_persp_2.setGeometry(QtCore.QRect(370, 30, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_persp_2.setFont(font)
        self.label_persp_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_persp_2.setObjectName("label_persp_2")
        self.topLeftx_silder = QtWidgets.QSlider(self.tab_perspective)
        self.topLeftx_silder.setGeometry(QtCore.QRect(180, 25, 150, 20))
        self.topLeftx_silder.setMinimum(-200)
        self.topLeftx_silder.setMaximum(200)
        self.topLeftx_silder.setSingleStep(10)
        self.topLeftx_silder.setOrientation(QtCore.Qt.Horizontal)
        self.topLeftx_silder.setObjectName("topLeftx_silder")
        self.topLefty_silder = QtWidgets.QSlider(self.tab_perspective)
        self.topLefty_silder.setGeometry(QtCore.QRect(180, 55, 150, 20))
        self.topLefty_silder.setMinimum(-200)
        self.topLefty_silder.setMaximum(200)
        self.topLefty_silder.setSingleStep(10)
        self.topLefty_silder.setOrientation(QtCore.Qt.Horizontal)
        self.topLefty_silder.setObjectName("topLefty_silder")
        self.bottomLeftx_silder = QtWidgets.QSlider(self.tab_perspective)
        self.bottomLeftx_silder.setGeometry(QtCore.QRect(180, 90, 150, 20))
        self.bottomLeftx_silder.setMinimum(-200)
        self.bottomLeftx_silder.setMaximum(200)
        self.bottomLeftx_silder.setSingleStep(10)
        self.bottomLeftx_silder.setOrientation(QtCore.Qt.Horizontal)
        self.bottomLeftx_silder.setObjectName("bottomLeftx_silder")
        self.bottomLefty_silder = QtWidgets.QSlider(self.tab_perspective)
        self.bottomLefty_silder.setGeometry(QtCore.QRect(180, 120, 150, 20))
        self.bottomLefty_silder.setMinimum(-200)
        self.bottomLefty_silder.setMaximum(200)
        self.bottomLefty_silder.setSingleStep(10)
        self.bottomLefty_silder.setOrientation(QtCore.Qt.Horizontal)
        self.bottomLefty_silder.setObjectName("bottomLefty_silder")
        self.topRightx_silder = QtWidgets.QSlider(self.tab_perspective)
        self.topRightx_silder.setGeometry(QtCore.QRect(540, 25, 150, 20))
        self.topRightx_silder.setMinimum(-200)
        self.topRightx_silder.setMaximum(200)
        self.topRightx_silder.setSingleStep(10)
        self.topRightx_silder.setOrientation(QtCore.Qt.Horizontal)
        self.topRightx_silder.setObjectName("topRightx_silder")
        self.topRighty_silder = QtWidgets.QSlider(self.tab_perspective)
        self.topRighty_silder.setGeometry(QtCore.QRect(540, 55, 150, 20))
        self.topRighty_silder.setMinimum(-200)
        self.topRighty_silder.setMaximum(200)
        self.topRighty_silder.setSingleStep(10)
        self.topRighty_silder.setOrientation(QtCore.Qt.Horizontal)
        self.topRighty_silder.setObjectName("topRighty_silder")
        self.bottomRightx_silder = QtWidgets.QSlider(self.tab_perspective)
        self.bottomRightx_silder.setGeometry(QtCore.QRect(540, 90, 150, 20))
        self.bottomRightx_silder.setMinimum(-200)
        self.bottomRightx_silder.setMaximum(200)
        self.bottomRightx_silder.setSingleStep(10)
        self.bottomRightx_silder.setOrientation(QtCore.Qt.Horizontal)
        self.bottomRightx_silder.setObjectName("bottomRightx_silder")
        self.bottomRighty_silder = QtWidgets.QSlider(self.tab_perspective)
        self.bottomRighty_silder.setGeometry(QtCore.QRect(540, 120, 150, 20))
        self.bottomRighty_silder.setMinimum(-200)
        self.bottomRighty_silder.setMaximum(200)
        self.bottomRighty_silder.setSingleStep(10)
        self.bottomRighty_silder.setOrientation(QtCore.Qt.Horizontal)
        self.bottomRighty_silder.setObjectName("bottomRighty_silder")
        self.tabWidget_2.addTab(self.tab_perspective, "")
        self.tab_roi = QtWidgets.QWidget()
        self.tab_roi.setObjectName("tab_roi")
        self.b_roi = QtWidgets.QPushButton(self.tab_roi)
        self.b_roi.setGeometry(QtCore.QRect(90, 45, 210, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.b_roi.setFont(font)
        self.b_roi.setObjectName("b_roi")
        self.b_roi_2 = QtWidgets.QPushButton(self.tab_roi)
        self.b_roi_2.setGeometry(QtCore.QRect(410, 45, 210, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.b_roi_2.setFont(font)
        self.b_roi_2.setObjectName("b_roi_2")
        self.tabWidget_2.addTab(self.tab_roi, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1190, 0, 250, 900))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.Effects = QtWidgets.QWidget()
        self.Effects.setObjectName("Effects")
        self.toolBox = QtWidgets.QToolBox(self.Effects)
        self.toolBox.setGeometry(QtCore.QRect(40, 50, 171, 701))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("background-image: url(:/images/blue_pastel.jpg);")
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.page_1.setObjectName("page_1")
        self.b_grayscale = QtWidgets.QPushButton(self.page_1)
        self.b_grayscale.setGeometry(QtCore.QRect(5, 100, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_grayscale.setFont(font)
        self.b_grayscale.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n")
        self.b_grayscale.setObjectName("b_grayscale")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.page_2.setObjectName("page_2")
        self.b_hsv = QtWidgets.QPushButton(self.page_2)
        self.b_hsv.setGeometry(QtCore.QRect(5, 150, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_hsv.setFont(font)
        self.b_hsv.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "background-image: url(:/images/khaki.jpg);\n")
        self.b_hsv.setObjectName("b_hsv")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.page_3.setObjectName("page_3")
        self.b_negative = QtWidgets.QPushButton(self.page_3)
        self.b_negative.setGeometry(QtCore.QRect(5, 160, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_negative.setFont(font)
        self.b_negative.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n"
"")
        self.b_negative.setObjectName("b_negative")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 171, 461))
        self.page_4.setObjectName("page_4")
        self.b_binary = QtWidgets.QPushButton(self.page_4)
        self.b_binary.setGeometry(QtCore.QRect(5, 30, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_binary.setFont(font)
        self.b_binary.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);")
        self.b_binary.setObjectName("b_binary")
        self.b_binaryInv = QtWidgets.QPushButton(self.page_4)
        self.b_binaryInv.setGeometry(QtCore.QRect(5, 115, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_binaryInv.setFont(font)
        self.b_binaryInv.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n")
        self.b_binaryInv.setObjectName("b_binaryInv")
        self.b_binarytrunc = QtWidgets.QPushButton(self.page_4)
        self.b_binarytrunc.setGeometry(QtCore.QRect(5, 200, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_binarytrunc.setFont(font)
        self.b_binarytrunc.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n")
        self.b_binarytrunc.setObjectName("b_binarytrunc")
        self.b_binarytozero = QtWidgets.QPushButton(self.page_4)
        self.b_binarytozero.setGeometry(QtCore.QRect(5, 285, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_binarytozero.setFont(font)
        self.b_binarytozero.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n")
        self.b_binarytozero.setObjectName("b_binarytozero")
        self.b_binarytozeroInv = QtWidgets.QPushButton(self.page_4)
        self.b_binarytozeroInv.setGeometry(QtCore.QRect(5, 370, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_binarytozeroInv.setFont(font)
        self.b_binarytozeroInv.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-image: url(:/images/khaki.jpg);\n")
        self.b_binarytozeroInv.setObjectName("b_binarytozeroInv")
        self.toolBox.addItem(self.page_4, "")
        self.tabWidget.addTab(self.Effects, "")
        self.Filter = QtWidgets.QWidget()
        self.Filter.setObjectName("Filter")
        self.tabWidget.addTab(self.Filter, "")
        self.frame_2.raise_()
        self.frame.raise_()
        self.pushButton.raise_()
        self.logo.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1440, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("color: rgb(0, 0, 0);")
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setIcon(icon3)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionExit_2)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.b_reset = QtWidgets.QPushButton(self.frame)
        self.b_reset.setGeometry(QtCore.QRect(1030, 575, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(25)
        self.b_reset.setFont(font)
        self.b_reset.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-image: url(:/images/khaki.jpg);\n")
        self.b_reset.setObjectName("b_reset")
        self.label_imgproperty = QtWidgets.QLabel(self.frame)
        self.label_imgproperty.setGeometry(QtCore.QRect(180, 540, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_imgproperty.setFont(font)
        self.label_imgproperty.setStyleSheet("background-image: url(:/images/khaki.jpg);\n")
        self.label_imgproperty.setText("")
        self.label_imgproperty.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_imgproperty.setObjectName("label_imgproperty")
        self.label_imgproperty.setVisible(False)
        self.b_reset.raise_()
        self.label_imgproperty.raise_()
        self.toolBox_2 = QtWidgets.QToolBox(self.Filter)
        self.toolBox_2.setGeometry(QtCore.QRect(40, 50, 180, 701))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox_2.setFont(font)
        self.toolBox_2.setStyleSheet("background-image: url(:/images/blue_pastel.jpg);")
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_convolution = QtWidgets.QWidget()
        self.page_convolution.setGeometry(QtCore.QRect(0, 0, 180, 513))
        self.page_convolution.setObjectName("page_convolution")
        self.b_convolution = QtWidgets.QPushButton(self.page_convolution)
        self.b_convolution.setGeometry(QtCore.QRect(5, 100, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(13)
        self.b_convolution.setFont(font)
        self.b_convolution.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-image: url(:/images/khaki.jpg);\n")
        self.b_convolution.setObjectName("b_convolution")
        self.toolBox_2.addItem(self.page_convolution, "")
        self.page_averaging = QtWidgets.QWidget()
        self.page_averaging.setGeometry(QtCore.QRect(0, 0, 180, 513))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page_averaging.setFont(font)
        self.page_averaging.setObjectName("page_averaging")
        self.b_averaging = QtWidgets.QPushButton(self.page_averaging)
        self.b_averaging.setGeometry(QtCore.QRect(5, 150, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_averaging.setFont(font)
        self.b_averaging.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-image: url(:/images/khaki.jpg);\n")
        self.b_averaging.setObjectName("b_averaging")
        self.toolBox_2.addItem(self.page_averaging, "")
        self.page_median = QtWidgets.QWidget()
        self.page_median.setGeometry(QtCore.QRect(0, 0, 180, 466))
        self.page_median.setObjectName("page_median")
        self.b_median = QtWidgets.QPushButton(self.page_median)
        self.b_median.setGeometry(QtCore.QRect(5, 160, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_median.setFont(font)
        self.b_median.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-image: url(:/images/khaki.jpg);\n")
        self.b_median.setObjectName("b_median")
        self.toolBox_2.addItem(self.page_median, "")
        self.page_bilateral = QtWidgets.QWidget()
        self.page_bilateral.setGeometry(QtCore.QRect(0, 0, 180, 466))
        self.page_bilateral.setObjectName("page_bilateral")
        self.b_bilateral = QtWidgets.QPushButton(self.page_bilateral)
        self.b_bilateral.setGeometry(QtCore.QRect(10, 180, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_bilateral.setFont(font)
        self.b_bilateral.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-image: url(:/images/khaki.jpg);\n")
        self.b_bilateral.setObjectName("b_bilateral")
        self.toolBox_2.addItem(self.page_bilateral, "")
        self.page_gaussian = QtWidgets.QWidget()
        self.page_gaussian.setObjectName("page_gaussian")
        self.b_gaussian = QtWidgets.QPushButton(self.page_gaussian)
        self.b_gaussian.setGeometry(QtCore.QRect(10, 130, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_gaussian.setFont(font)
        self.b_gaussian.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-image: url(:/images/khaki.jpg);\n")
        self.b_gaussian.setObjectName("b_gaussian")
        self.toolBox_2.addItem(self.page_gaussian, "")
        self.page_laplacian = QtWidgets.QWidget()
        self.page_laplacian.setObjectName("page_laplacian")
        self.b_laplacian = QtWidgets.QPushButton(self.page_laplacian)
        self.b_laplacian.setGeometry(QtCore.QRect(10, 120, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_laplacian.setFont(font)
        self.b_laplacian.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-image: url(:/images/khaki.jpg);\n")
        self.b_laplacian.setObjectName("b_laplacian")
        self.toolBox_2.addItem(self.page_laplacian, "")
        self.page_sobelx = QtWidgets.QWidget()
        self.page_sobelx.setObjectName("page_sobelx")
        self.b_sobelx = QtWidgets.QPushButton(self.page_sobelx)
        self.b_sobelx.setGeometry(QtCore.QRect(10, 110, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_sobelx.setFont(font)
        self.b_sobelx.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-image: url(:/images/khaki.jpg);\n")
        self.b_sobelx.setObjectName("b_sobelx")
        self.toolBox_2.addItem(self.page_sobelx, "")
        self.page_sobely = QtWidgets.QWidget()
        self.page_sobely.setObjectName("page_sobely")
        self.b_sobely = QtWidgets.QPushButton(self.page_sobely)
        self.b_sobely.setGeometry(QtCore.QRect(10, 80, 160, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(15)
        self.b_sobely.setFont(font)
        self.b_sobely.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-image: url(:/images/khaki.jpg);\n")
        self.b_sobely.setObjectName("b_sobely")
        self.toolBox_2.addItem(self.page_sobely, "")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Image Editor"))
        self.label_original.setText(_translate("MainWindow", "Original"))
        self.label_processed.setText(_translate("MainWindow", "Processed"))
        self.pushButton.setText(_translate("MainWindow", "Save As..."))
        self.label_scale.setText(_translate("MainWindow", "Width Scale\t=\n\nHeight Scale\t="))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_resize), _translate("MainWindow", "Resize"))
        self.b_rotateLeft.setText(_translate("MainWindow", "Rotate Left 90°"))
        self.b_rotateRight.setText(_translate("MainWindow", "Rotate Right 90°"))
        self.b_rotate180.setText(_translate("MainWindow", "Rotate 180°"))
        self.b_flipVertical.setText(_translate("MainWindow", "Flip Vertical"))
        self.b_flipHori.setText(_translate("MainWindow", "Flip Horizontal"))
        self.sliderLabel.setText(_translate("MainWindow", "0°"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_rotate), _translate("MainWindow", "Rotate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_perspective),
                                    _translate("MainWindow", "Perspective"))
        self.label_persp.setText(_translate("MainWindow", "topLeft_x\t:\n"
                                                          "topLeft_y\t:\n\n"
                                                          "bottomLeft_x\t:\n"
                                                          "bottomLeft_y\t:"))
        self.label_persp_2.setText(_translate("MainWindow", "topRight_x\t:\n"
                                                            "topRight_y\t:\n\n"
                                                            "bottomRight_x\t:\n"
                                                            "bottomRight_y\t:"))
        self.b_roi.setText(_translate("MainWindow", "select region"))
        self.b_roi_2.setText(_translate("MainWindow", "auto RoI"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_roi),
                                    _translate("MainWindow", "Region of Interest"))
        self.b_grayscale.setText(_translate("MainWindow", "change to \n"
                                                          "grayscale"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("MainWindow", "Grayscale"))
        self.b_hsv.setText(_translate("MainWindow", "change to \n"
                                                    "HSV"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "   HSV"))
        self.b_negative.setText(_translate("MainWindow", "change to \n"
                                                         "negative"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", " Negative"))
        self.b_binary.setText(_translate("MainWindow", "binary"))
        self.b_binaryInv.setText(_translate("MainWindow", "binary,\n"
                                                          "inverted"))
        self.b_binarytrunc.setText(_translate("MainWindow", "binary, \n"
                                                            "truncate"))
        self.b_binarytozero.setText(_translate("MainWindow", "to Zero"))
        self.b_binarytozeroInv.setText(_translate("MainWindow", "to Zero, \n"
                                                                "inverted"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Threshold"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Effects), _translate("MainWindow", "Effects"))
        self.b_convolution.setText(_translate("MainWindow", "filter to \n"
                                                            "2D convolution"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_convolution),
                                   _translate("MainWindow", "2D Convolution"))
        self.b_averaging.setText(_translate("MainWindow", "filter to \n"
                                                          "averaging"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_averaging),
                                   _translate("MainWindow", "   Averaging"))
        self.b_median.setText(_translate("MainWindow", "filter to \n"
                                                       "median"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_median), _translate("MainWindow", "     Median"))
        self.b_bilateral.setText(_translate("MainWindow", "filter to\n"
                                                          "bilateral"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_bilateral),
                                   _translate("MainWindow", "    Bilateral"))
        self.b_gaussian.setText(_translate("MainWindow", "filter to\n"
                                                         "gaussian"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_gaussian), _translate("MainWindow", "    Gaussian"))
        self.b_laplacian.setText(_translate("MainWindow", "filter to\n"
                                                          "laplacian"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_laplacian),
                                   _translate("MainWindow", "    Laplacian"))
        self.b_sobelx.setText(_translate("MainWindow", "filter to\n"
                                                       "sobel_x"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_sobelx), _translate("MainWindow", "    Sobel_x"))
        self.b_sobely.setText(_translate("MainWindow", "filter to\n"
                                                       "sobel_y"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_sobely), _translate("MainWindow", "    Sobel_y"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Filter), _translate("MainWindow", "Filter"))
        self.menu_File.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open.."))
        self.actionExit_2.setText(_translate("MainWindow", "Exit.."))
        self.b_reset.setText(_translate("MainWindow", "Reset "))
        self.label_imgproperty.setText(_translate("MainWindow", " "))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        self.allButtonFnction()


    def allButtonFnction(self):
        self.b_reset.clicked.connect(self.resetAll)
        self.actionOpen.triggered.connect(self.loadImage)

        # effects clicked
        self.b_grayscale.clicked.connect(self.imgToGray)
        self.b_hsv.clicked.connect(self.imgToHSV)
        self.b_negative.clicked.connect(self.imgToNegative)
        self.b_binary.clicked.connect(self.imgToBinary)
        self.b_binaryInv.clicked.connect(self.imgToBinaryInv)
        self.b_binarytrunc.clicked.connect(self.imgToTruncate)
        self.b_binarytozero.clicked.connect(self.imgToZero)
        self.b_binarytozeroInv.clicked.connect(self.imgToZeroInv)

        # filter clicked
        self.b_convolution.clicked.connect(self.imgToConvolution)
        self.b_averaging.clicked.connect(self.imgToAveraging)
        self.b_median.clicked.connect(self.imgToMedian)
        self.b_bilateral.clicked.connect(self.imgToBilateral)
        self.b_gaussian.clicked.connect(self.imgToGaussian)
        self.b_laplacian.clicked.connect(self.imgToLaplacian)
        self.b_sobelx.clicked.connect(self.imgToSobelx)
        self.b_sobely.clicked.connect(self.imgToSobely)

        # rotate_call
        self.b_rotateLeft.clicked.connect(self.img_rotateLeft)
        self.b_rotateRight.clicked.connect(self.img_rotateRight)
        self.b_rotate180.clicked.connect(self.img_rotate180)
        self.b_flipVertical.clicked.connect(self.img_flipVertical)
        self.b_flipHori.clicked.connect(self.img_flipHorizontal)
        self.rotateSlider.valueChanged.connect(self.img_rotateUseSlider)

        #resize
        self.widthSlider.valueChanged.connect(self.img_resize)
        self.heightSlider.valueChanged.connect(self.img_resize)

        #perspective
        self.topLeftx_silder.valueChanged.connect(self.img_perspective)
        self.topLefty_silder.valueChanged.connect(self.img_perspective)
        self.topRightx_silder.valueChanged.connect(self.img_perspective)
        self.topRighty_silder.valueChanged.connect(self.img_perspective)
        self.bottomLeftx_silder.valueChanged.connect(self.img_perspective)
        self.bottomLefty_silder.valueChanged.connect(self.img_perspective)
        self.bottomRightx_silder.valueChanged.connect(self.img_perspective)
        self.bottomRighty_silder.valueChanged.connect(self.img_perspective)

        self.b_roi.clicked.connect(self.img_roi)
        self.b_roi_2.clicked.connect(self.img_autoRoi)
        self.pushButton.clicked.connect(self.saveImage)
        self.actionExit_2.triggered.connect(self.closeApp)
        self.actionAbout.triggered.connect(self.aboutApps)

# **********************************load, save, reset, close function****************************************************
    def loadImage(self, MainWindow):
        global image
        image = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'D:\\')[0]
        pixmap = QtGui.QPixmap(image)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.label_1.setPixmap(scaledImage)
        img = cv2.imread(image)
        height, width, channel = img.shape
        self.label_imgproperty.setVisible(True)
        self.label_imgproperty.setText(
            "         Image Properties\nWidth\t: " + str(height) + "\nHeight\t: " + str(width) +
            "\nChannel\t: " + str(channel))


    def saveImage(self):
        try:
            fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'D:\\', "Image Files (*.jpg)")
            if fname:
                cv2.imwrite(fname, b)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Image successfuly saved")
                msg.setWindowTitle("Image Saved")
                msg.setDetailedText("The image path is : " + "\"" + fname + "\"")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
            else:
                print('Error')
        except:
            self.error()
    def resetAll(self):
        self.label_1.clear()
        self.label_2.clear()
        self.label_imgproperty.clear()
        self.label_imgproperty.setVisible(False)
        white = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
        cv2.imwrite("white.jpg", white)
        b =cv2.imread("white.jpg")

    def rgb_update(self, b):
        c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap(c)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(scaledImage)

    def gray_update(self, b):
        c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1], QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(c)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(scaledImage)


    def closeApp(self):
        msg = QtWidgets.QMessageBox.question(self, 'Exit Confirmation', "Are you want to Quit?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            return

    def error(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Where is your IMAGE dude?!")
        msg.setWindowTitle("ERROr!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    # ******************************effects function*************************************************************************
    def imgToGray(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            self.gray_update(b)
        except:
            self.error()

    def imgToHSV(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.cvtColor(a, cv2.COLOR_RGB2HSV)
            c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1] * 3, QImage.Format_RGB888)
            pixmap = QtGui.QPixmap(c)
            scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(scaledImage)
        except:
            self.error()

    def imgToBinary(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            self.gray_update(b)
        except:
            self.error()

    def imgToBinaryInv(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            self.gray_update(b)
        except:
            self.error()

    def imgToTruncate(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
            self.gray_update(b)
        except:
            self.error()

    def imgToZero(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
            self.gray_update(b)
        except:
            self.error()

    def imgToZeroInv(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
            self.gray_update(b)
        except:
            self.error()
    def imgToNegative(self):
        global b
        try:
            S = 255
            img = cv2.imread(image)
            B, G, R = cv2.split(img)
            B[:] = [S - x for x in B]  # inverting blue
            G[:] = [S - x for x in G]  # inverting green
            R[:] = [S - x for x in R]  # inverting red
            b = cv2.merge((B, G, R))
            self.rgb_update(b)
        except:
            self.error()

    # **********************************filter function**********************************************************************
    def imgToConvolution(self):
        global b
        try:
            a = cv2.imread(image)
            kernel = np.ones((5, 5), np.float32) / 25
            b = cv2.filter2D(a, -1, kernel)
            self.rgb_update(b)
        except:
            self.error()

    def imgToAveraging(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.blur(a, (5, 5))
            self.rgb_update(b)
        except:
            self.error()

    def imgToMedian(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.medianBlur(a, 5)
            self.rgb_update(b)
        except:
            self.error()

    def imgToBilateral(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.bilateralFilter(a, 9, 75, 75)
            self.rgb_update(b)
        except:
            self.error()

    def imgToGaussian(self):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.GaussianBlur(a, (5, 5), 0)
            self.rgb_update(b)
        except:
            self.error()

    def imgToLaplacian(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
            laplacian = cv2.Laplacian(gray, cv2.CV_8U)
            b = cv2.cvtColor(laplacian, cv2.COLOR_BGR2RGB)
            self.rgb_update(b)
        except:
            self.error()

    def imgToSobelx(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
            sobelx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=5)
            b = cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB)
            self.rgb_update(b)
        except:
            self.error()

    def imgToSobely(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
            sobely = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=5)
            b = cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB)
            self.rgb_update(b)
        except:
            self.error()
    # ***************************************rotate function*****************************************************************
    def rotatefnc(self, angle):
        global b
        try:
            a = cv2.imread(image)
            h, w = a.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, angle, 1)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            framew = int((h * sin) + (w * cos))
            frameh = int((h * cos) + (w * sin))
            M[0, 2] += ((framew / 2) - center[0])
            M[1, 2] += ((frameh / 2) - center[1])
            b = cv2.warpAffine(a, M, (framew, frameh))
            self.rgb_update(b)
        except:
            self.error()

    def img_rotateUseSlider(self):
        self.rotatefnc(self.rotateSlider.value())
        self.sliderLabel.setText(str(self.rotateSlider.value()) + "°")

    def img_rotateLeft(self):
        self.rotatefnc(90)

    def img_rotateRight(self):
        self.rotatefnc(-90)

    def img_rotate180(self):
        self.rotatefnc(180)

    def img_flip(self, flipcode):
        global b
        try:
            a = cv2.imread(image)
            b = cv2.flip(a, flipcode)
            self.rgb_update(b)
        except:
            self.error()

    def img_flipVertical(self):
        self.img_flip(0)

    def img_flipHorizontal(self):
        self.img_flip(1)

    def img_resize(self):
        global b
        try:
            a = cv2.imread(image)
            h, w, c = a.shape
            Wscale = (self.widthSlider.value()) / 10
            Hscale = (self.heightSlider.value()) / 10
            newW, newH = w * Wscale, h * Hscale
            b = cv2.resize(a, (int(newW), int(newH)))
            self.rgb_update(b)
            self.label_scale.setText("Width Scale\t= " + str(Wscale) + "\n\nHeight Scale\t= " + str(Hscale))
        except:
            self.error()

    def img_perspective(self):
        global b
        try:
            a = cv2.imread(image)
            newimg = cv2.resize(a, (500, 375))
            tLx = self.topLeftx_silder.value()
            tLy = self.topLefty_silder.value()
            tRx = self.topRightx_silder.value()
            tRy = self.topRighty_silder.value()
            bLx = self.bottomLeftx_silder.value()
            bLy = self.bottomLefty_silder.value()
            bRx = self.bottomRightx_silder.value()
            bRy = self.bottomRighty_silder.value()
            p1 = np.float32([[0, 0], [500, 0], [0, 375], [500, 375]])
            # p2 = np.float32([[100, 0], [300, 0], [0, 375], [500, 375]])
            p2 = np.float32([[0 + tLx, 0 + tLy], [500 + tRx, 0 + tRy], [0 + bLx, 375 + bLy], [500 + bRx, 375 + bRy]])
            matrix = cv2.getPerspectiveTransform(p1, p2)
            b = cv2.warpPerspective(newimg, matrix, (500, 375))
            self.rgb_update(b)
        except:
            self.error()

    def img_roi(self):
        global b
        try:
            a = cv2.imread(image)
            fromCenter = False
            r = cv2.selectROI("image", a, fromCenter)
            roi = a[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            cv2.waitKey(1000)
            cv2.imwrite("roi.jpg", roi)
            b = cv2.imread("roi.jpg")
            self.rgb_update(b)
            os.remove("roi.jpg")
            cv2.destroyAllWindows()
        except:
            self.error()

    def img_autoRoi(self):
        global b
        try:
            a = cv2.imread(image)
            gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            kernel = np.ones((10, 1), np.uint8)
            img_dilation = cv2.dilate(thresh, kernel, iterations=1)
            cv2MajorVersion = cv2.__version__.split(".")[0]
            if int(cv2MajorVersion) >= 4:
                ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            else:
                im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
            for i, ctr in enumerate(sorted_ctrs):
                x, y, w, h = cv2.boundingRect(ctr)
                roi = a[y:y + h, x:x + w]
                cv2.rectangle(a, (x, y), (x + w, y + h), (0, 255, 0), 2)

            b = a
            self.rgb_update(b)
        except:
            self.error()

    def aboutApps(self):
        self.window = QtWidgets.QDialog()
        self.ex = Ui_Dialog()
        self.ex.setupUi2(self.window)
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())

