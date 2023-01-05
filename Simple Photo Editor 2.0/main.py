from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import resources, sys, cv2, numpy as np
import os
from about import Ui_Dialog
from gui import Ui_MainWindow
from matplotlib import pyplot as plt
image = ""
b = ""


class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.imageTemp = ""
        self.imageOri = ""


        # menu bar function
        self.actionOpen.triggered.connect(self.loadImage)               # load image
        self.actionExit_2.triggered.connect(self.closeApp)              # exit
        self.actionAbout.triggered.connect(self.aboutApps)              # about apps
        self.actionOriginal.triggered.connect(self.histogram_Ori)       # original histogram
        self.actionProcessed.triggered.connect(self.histogram_process)  # processed histogram
        self.actionEqualization.triggered.connect(self.hist_equal)      # equalize histogram


        self.b_reset.clicked.connect(self.resetAll)                     # clear label
        self.pushButton.clicked.connect(self.saveImage)                 # save image

        # effects clicked
        self.b_grayscale.clicked.connect(self.imgToGray)
        self.b_hsv.clicked.connect(self.imgToHSV)
        self.b_negative.clicked.connect(self.imgToNegative)
        self.b_binary.clicked.connect(self.imgToBinary)
        self.b_binaryInv.clicked.connect(self.imgToBinaryInv)
        self.b_binarytrunc.clicked.connect(self.imgToTruncate)
        self.b_binarytozero.clicked.connect(self.imgToZero)
        self.b_binarytozeroInv.clicked.connect(self.imgToZeroInv)
        self.b_roi1.clicked.connect(self.img_roi)
        self.b_roi2.clicked.connect(self.img_autoRoi)

        # filter clicked
        self.b_convolution.clicked.connect(self.imgToConvolution)
        self.b_averaging.clicked.connect(self.imgToAveraging)
        self.b_median.clicked.connect(self.imgToMedian)
        self.b_bilateral.clicked.connect(self.imgToBilateral)
        self.b_gaussian.clicked.connect(self.imgToGaussian)
        self.b_laplacian.clicked.connect(self.imgToLaplacian)
        self.b_sobelx.clicked.connect(self.imgToSobelx)
        self.b_sobely.clicked.connect(self.imgToSobely)
        self.b_cannye.clicked.connect(self.cannyEdge)
        self.b_sobele.clicked.connect(self.sobelEdge)
        self.b_prewitte.clicked.connect(self.prewittEdge)
        self.median_slider.valueChanged.connect(self.imgToMedian)
        self.bilateral_slider.valueChanged.connect(self.imgToBilateral)
        self.gaussian_slider.valueChanged.connect(self.imgToGaussian)

        # rotate_call
        self.b_rotateLeft.clicked.connect(self.img_rotateLeft)
        self.b_rotateRight.clicked.connect(self.img_rotateRight)
        self.b_rotate180.clicked.connect(self.img_rotate180)
        self.b_flipVertical.clicked.connect(self.img_flipVertical)
        self.b_flipHori.clicked.connect(self.img_flipHorizontal)
        self.rotateSlider.valueChanged.connect(self.img_rotateUseSlider)

        # resize
        self.widthSlider.valueChanged.connect(self.img_resize)
        self.heightSlider.valueChanged.connect(self.img_resize)

        # perspective
        self.topLeftx_silder.valueChanged.connect(self.img_perspective)
        self.topLefty_silder.valueChanged.connect(self.img_perspective)
        self.topRightx_silder.valueChanged.connect(self.img_perspective)
        self.topRighty_silder.valueChanged.connect(self.img_perspective)
        self.bottomLeftx_silder.valueChanged.connect(self.img_perspective)
        self.bottomLefty_silder.valueChanged.connect(self.img_perspective)
        self.bottomRightx_silder.valueChanged.connect(self.img_perspective)
        self.bottomRighty_silder.valueChanged.connect(self.img_perspective)

        # split_image
        self.spinBox_row.valueChanged.connect(self.split_image)
        self.spinBox_column.valueChanged.connect(self.split_image)
        self.splitButton.clicked.connect(self.plot_split)
        self.line_cbox.currentTextChanged.connect(self.split_image)
        self.saveSplit.clicked.connect(self.saveSplitImage)

        # merge_image
        self.count_cbox.currentTextChanged.connect(self.loadImgNum)
        self.load_img2.clicked.connect(self.img2_load)
        self.load_img3.clicked.connect(self.img3_load)
        self.load_img4.clicked.connect(self.img4_load)
        self.merge_button.clicked.connect(self.showall)

        # binary_morphology
        self.dilation_slider.valueChanged.connect(self.getDilationSliderValue)
        self.b_dilate.clicked.connect(self.dilationClicked)
        self.erosion_slider.valueChanged.connect(self.getErosionSliderValue)
        self.b_erode.clicked.connect(self.erosionClicked)

        self.b_halftone.clicked.connect(self.imgToHafltone)


# **********************************load, save, reset, close function****************************************************
    def loadImage(self, MainWindow):
        global image
        try:
            image = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'C:\\')[0]
            pixmap = QtGui.QPixmap(image)
            scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
            self.label_1.setPixmap(scaledImage)
            img = cv2.imread(image)
            height, width, channel = img.shape
            self.label_imgproperty.setVisible(True)
            self.label_imgproperty.setText(
                "         Image Properties\nWidth\t: " + str(width) + "\nHeight\t: " + str(height) +
                "\nChannel\t: " + str(channel))
            self.imageTemp = cv2.imread(image)
            self.imageOri = cv2.imread(image)
        except:
            self.error()

    def checkImage(self, checkimage):
        if len(checkimage.shape) ==3:
            self.imageTemp = checkimage
        else:
            c = cv2.cvtColor(checkimage, cv2.COLOR_GRAY2BGR)
            self.imageTemp = c
        return self.imageTemp

    def saveImage(self):
        try:
            fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\', "Image Files (*.jpg);;Bitmap(*.bmp);;PNG(*.png);;TIFF(*.tiff)")
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
        self.checkImage(self.imageOri)
        self.displayImage(self.imageOri)


    def displayImage(self, b):
        if len(b.shape) ==3 :
            c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        else:
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
        msg.setText("Where is your IMAGE?!")
        msg.setWindowTitle("ERROR!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    # ******************************effects function*************************************************************************
    def imgToGray(self):
        global b
        try:
            b = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToHSV(self):
        global b
        try:
            b = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2HSV)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToBinary(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToBinaryInv(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToTruncate(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToZero(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToZeroInv(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
            ret, b = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToNegative(self):
        global b
        try:
            S = 255
            B, G, R = cv2.split(self.imageTemp)
            B[:] = [S - x for x in B]  # inverting blue
            G[:] = [S - x for x in G]  # inverting green
            R[:] = [S - x for x in R]  # inverting red
            b = cv2.merge((B, G, R))
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    # **********************************filter function**********************************************************************
    def imgToConvolution(self):
        global b
        try:
            kernel = np.ones((5, 5), np.float32) / 25
            b = cv2.filter2D(self.imageTemp, -1, kernel)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToAveraging(self):
        global b
        try:
            b = cv2.blur(self.imageTemp, (5, 5))
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def getMedianSliderValue(self):
        if int(self.median_slider.value()) %2 == 1:
            return int(self.median_slider.value())
        else:
            return int(self.median_slider.value())+1

    def imgToMedian(self):
        global b
        self.median_kernel.setText("kernel = "+str(self.getMedianSliderValue()))
        try:
            b = cv2.medianBlur(self.imageTemp, self.getMedianSliderValue())
            self.displayImage(b)
        except:
            self.error()

    def getBilateralSliderValue(self):
        if int(self.bilateral_slider.value()) %2 == 1:
            return int(self.bilateral_slider.value())
        else:
            return int(self.bilateral_slider.value())+1

    def imgToBilateral(self):
        global b
        self.bilateral_kernel.setText("kernel = "+str(self.getBilateralSliderValue())+", "+str(self.getBilateralSliderValue()))
        try:
            b = cv2.bilateralFilter(self.imageTemp, 9, self.getBilateralSliderValue(), self.getBilateralSliderValue())
            self.displayImage(b)
        except:
            self.error()

    def getGaussianSliderValue(self):
        if int(self.gaussian_slider.value()) %2 == 1:
            return int(self.gaussian_slider.value())
        else:
            return int(self.gaussian_slider.value())+1

    def imgToGaussian(self):
        global b
        self.gaussian_kernel.setText("kernel = (" + str(self.getGaussianSliderValue()) + ", " + str(self.getGaussianSliderValue())+")")
        try:
            b = cv2.GaussianBlur(self.imageTemp, (self.getGaussianSliderValue(), self.getGaussianSliderValue()), 0)
            self.displayImage(b)
        except:
            self.error()

    def imgToLaplacian(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2GRAY)
            laplacian = cv2.Laplacian(gray, cv2.CV_8U)
            b = cv2.cvtColor(laplacian, cv2.COLOR_BGR2RGB)
            self.checkImage(b)
            self.displayImage(b)

        except:
            self.error()

    def imgToSobelx(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2GRAY)
            sobelx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=5)
            b = cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def imgToSobely(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2GRAY)
            sobely = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=5)
            b = cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()
    # ***************************************rotate function*****************************************************************
    def rotatefnc(self, angle):
        global b
        try:
            h, w = self.imageTemp.shape[:2]
            center = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center, angle, 1)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            framew = int((h * sin) + (w * cos))
            frameh = int((h * cos) + (w * sin))
            M[0, 2] += ((framew / 2) - center[0])
            M[1, 2] += ((frameh / 2) - center[1])
            b = cv2.warpAffine(self.imageTemp, M, (framew, frameh))
            self.checkImage(b)
            self.displayImage(b)
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
            b = cv2.flip(self.imageTemp, flipcode)
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def img_flipVertical(self):
        self.img_flip(0)

    def img_flipHorizontal(self):
        self.img_flip(1)

    def img_resize(self):
        global b
        try:
            t = cv2.imread(image)
            h, w, c =t.shape
            Wscale = (self.widthSlider.value()) / 10
            Hscale = (self.heightSlider.value()) / 10
            newW, newH = w * Wscale, h * Hscale
            b = cv2.resize(t, (int(newW), int(newH)))
            self.checkImage(b)
            self.displayImage(b)
            self.label_scale.setText("Width Scale\t= " + str(Wscale) + "\n\nHeight Scale\t= " + str(Hscale))
        except:
            self.error()

    def img_perspective(self):
        global b
        try:
            newimg = cv2.resize(self.imageTemp, (500, 375))
            tLx = self.topLeftx_silder.value()
            tLy = self.topLefty_silder.value()
            tRx = self.topRightx_silder.value()
            tRy = self.topRighty_silder.value()
            bLx = self.bottomLeftx_silder.value()
            bLy = self.bottomLefty_silder.value()
            bRx = self.bottomRightx_silder.value()
            bRy = self.bottomRighty_silder.value()
            p1 = np.float32([[0, 0], [500, 0], [0, 375], [500, 375]])
            p2 = np.float32([[0 + tLx, 0 + tLy], [500 + tRx, 0 + tRy], [0 + bLx, 375 + bLy], [500 + bRx, 375 + bRy]])
            matrix = cv2.getPerspectiveTransform(p1, p2)
            b = cv2.warpPerspective(newimg, matrix, (500, 375))
            self.displayImage(b)
        except:
            self.error()

    def img_roi(self):
        global b
        try:
            fromCenter = False
            r = cv2.selectROI("image", self.imageTemp, fromCenter)
            roi = self.imageTemp[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
            cv2.waitKey(1000)
            cv2.imwrite("roi.jpg", roi)
            b = cv2.imread("roi.jpg")
            self.checkImage(b)
            self.displayImage(b)
            os.remove("roi.jpg")
            cv2.destroyAllWindows()
        except:
            self.error()

    def img_autoRoi(self):
        global b
        try:
            gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
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
                roi = self.imageTemp[y:y + h, x:x + w]
                cv2.rectangle(self.imageTemp, (x, y), (x + w, y + h), (0, 255, 0), 2)
            b = self.imageTemp
            self.checkImage(b)
            self.displayImage(b)
        except:
            self.error()

    def aboutApps(self):
        self.window = QtWidgets.QDialog()
        self.ex = Ui_Dialog()
        self.ex.setupUi2(self.window)
        self.window.show()

    #*************************************** Histogram *****************************************************************
    def histogram_Ori(self):
        try:
            rgb, bins = np.histogram((self.imageTemp).ravel(), 256, [0, 256])
            blue = cv2.calcHist([self.imageTemp], [0], None, [256], [0, 256])
            green = cv2.calcHist([self.imageTemp], [1], None, [256], [0, 256])
            red = cv2.calcHist([self.imageTemp], [2], None, [256], [0, 256])
            plt.figure("Histogram of Original Image")
            plt.subplot(2, 3, 1)
            plt.plot(rgb, color='k')
            plt.title("rgb")
            plt.subplot(2, 3, 2)
            plt.plot(blue, color='b')
            plt.title("blue")
            plt.subplot(2, 3, 3)
            plt.plot(green, color='g')
            plt.title("green")
            plt.subplot(2, 3, 4)
            plt.plot(red, color='r')
            plt.title("red")
            color = ('b', 'g', 'r')
            for i, col in enumerate(color):
                colors = cv2.calcHist([self.imageTemp], [i], None, [256], [0, 256])
                plt.subplot(2, 3, 5)
                plt.plot(colors, color=col)
                plt.title("colors")
            # plt.xlim([0, 256])
            plt.show()
        except:
            self.error()

    def histogram_process(self):
        try:
            if len(b.shape) == 3:
                rgb, bins = np.histogram(b.ravel(), 256, [0, 256])
                blue = cv2.calcHist([b], [0], None, [256], [0, 256])
                green = cv2.calcHist([b], [1], None, [256], [0, 256])
                red = cv2.calcHist([b], [2], None, [256], [0, 256])
                plt.figure("Histogram of Processed Image")
                plt.subplot(2, 3, 1)
                plt.plot(rgb, color='k')
                plt.title("rgb")
                plt.subplot(2, 3, 2)
                plt.plot(blue, color='b')
                plt.title("blue")
                plt.subplot(2, 3, 3)
                plt.plot(green, color='g')
                plt.title("green")
                plt.subplot(2, 3, 4)
                plt.plot(red, color='r')
                plt.title("red")
                color = ('b', 'g', 'r')
                for i, col in enumerate(color):
                    colors = cv2.calcHist([b], [i], None, [256], [0, 256])
                    plt.subplot(2, 3, 5)
                    plt.plot(colors, color=col)
                    plt.title("colors")
                # plt.xlim([0, 256])
                plt.show()
            else:
                gray = cv2.calcHist([b], [0], None, [256], [0, 256])
                plt.figure("Histogram of processed image")
                plt.subplot(2, 3, 2)
                plt.plot(gray, color='k')
                plt.title("gray channel")
                plt.show()
        except:
            self.error()

    def hist_equal(self):
        global b
        try:
            bb,gg,rr = cv2.split(self.imageTemp)
            eb = cv2.equalizeHist(bb)
            eg = cv2.equalizeHist(gg)
            er = cv2.equalizeHist(rr)
            b = cv2.merge((eb,eg,er))
            self.checkImage(b)
            self.displayImage(b)
            equalize_histogram, _ = np.histogram(b.ravel(), 256, [0, 256])
            blue = cv2.calcHist([b], [0], None, [256], [0, 256])
            green = cv2.calcHist([b], [1], None, [256], [0, 256])
            red = cv2.calcHist([b], [2], None, [256], [0, 256])
            plt.figure("Equalization Histogram")
            plt.subplot(2, 3, 1)
            plt.plot(equalize_histogram, color='k')
            plt.title("rgb")
            plt.subplot(2, 3, 2)
            plt.plot(blue, color='b')
            plt.title("blue")
            plt.subplot(2, 3, 3)
            plt.plot(green, color='g')
            plt.title("green")
            plt.subplot(2, 3, 4)
            plt.plot(red, color='r')
            plt.title("red")
            color = ('b', 'g', 'r')
            for i, col in enumerate(color):
                colors = cv2.calcHist([b], [i], None, [256], [0, 256])
                plt.subplot(2, 3, 5)
                plt.plot(colors, color=col)
                plt.title("colors")
            plt.show()
        except:
            self.error()

    #******************************* split image ***********************************************************************
    def lineColor(self):
        if self.line_cbox.currentText() == "yellow":
            color = (0, 255, 255)
            return color
        elif self.line_cbox.currentText() == "black":
            color = (0, 0, 0)
            return color
        elif self.line_cbox.currentText() == "white":
            color = (255, 255, 255)
            return color
        else:
            color = (0, 255, 0)
            return color

    def split_image(self):
        lol = cv2.imread(image)
        a_height = lol.shape[0]
        a_width = lol.shape[1]
        y1 = 0
        r = self.spinBox_row.value()
        c = self.spinBox_column.value()
        M = a_height // r
        N = a_width // c
        k = 0
        for y in range(0, a_height, M):
            for x in range(0, a_width, N):
                k += 1
                y1 = y + M
                x1 = x + N
                cv2.rectangle(lol, (x, y), (x1, y1), self.lineColor())
        c = QtGui.QImage(lol, lol.shape[1], lol.shape[0], lol.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        pixmap = QtGui.QPixmap(c)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_2.setPixmap(scaledImage)

    def plot_split(self):
        lol = cv2.imread(image)
        a_height = lol.shape[0]
        a_width = lol.shape[1]
        r = self.spinBox_row.value()
        c = self.spinBox_column.value()
        M = a_height // r
        N = a_width // c
        k = 0
        if a_height%r or a_width %c !=0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Unable to split\nsplit image has small remainder\nchoose other value of row/column")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            for y in range(0, a_height, M):
                for x in range(0, a_width, N):
                    k += 1
                    tiles = lol[y:y + M, x:x + N]
                    gg = cv2.cvtColor(tiles, cv2.COLOR_BGR2RGB)
                    # cv2.imwrite("split"+str(x)+"_"+str(y)+".jpg", tiles)
                    plt.subplot(r, c, k)
                    plt.imshow(gg)
                    plt.xticks([]), plt.yticks([])
            plt.show()

    def saveSplitImage(self):
        lol = cv2.imread(image)
        a_height = lol.shape[0]
        a_width = lol.shape[1]
        r = self.spinBox_row.value()
        c = self.spinBox_column.value()
        M = a_height // r
        N = a_width // c
        k = 0
        if a_height % r or a_width % c != 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Unable to split\nsplit image has small remainder\nchoose other value of row/column")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            for y in range(0, a_height, M):
                for x in range(0, a_width, N):
                    k += 1
                    tiles = lol[y:y + M, x:x + N]
                    cv2.imwrite("split"+str(x)+"_"+str(y)+".jpg", tiles)

    #********************************** merge image ********************************************************************
    def img2_load(self): # load img2
        self.img2 = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'C:\\')[0]
        pixmap = QtGui.QPixmap(self.img2)
        scaledImage = pixmap.scaled(100, 75, QtCore.Qt.KeepAspectRatio)
        self.label_img2.setPixmap(scaledImage)

    def img3_load(self): # load img3
        self.img3 = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'C:\\')[0]
        pixmap = QtGui.QPixmap(self.img3)
        scaledImage = pixmap.scaled(100, 75, QtCore.Qt.KeepAspectRatio)
        self.label_img3.setPixmap(scaledImage)

    def img4_load(self): # load img3
        self.img4 = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'C:\\')[0]
        pixmap = QtGui.QPixmap(self.img4)
        scaledImage = pixmap.scaled(100, 75, QtCore.Qt.KeepAspectRatio)
        self.label_img4.setPixmap(scaledImage)

    def loadImgNum(self):
        if self.count_cbox.currentText()=="2":
            self.label_img3.setVisible(False), self.load_img3.setVisible(False)
            self.label_img4.setVisible(False), self.load_img4.setVisible(False)
            self.label_img2.setVisible(True),self.load_img2.setVisible(True)
            self.label_img3.clear(), self.label_img4.clear()

        elif self.count_cbox.currentText()=="3":
            self.label_img4.setVisible(False), self.load_img4.setVisible(False)
            self.label_img2.setVisible(True), self.load_img2.setVisible(True)
            self.label_img3.setVisible(True), self.load_img3.setVisible(True)
            self.label_img4.clear()

        elif self.count_cbox.currentText()=="4":
            self.label_img2.setVisible(True), self.load_img2.setVisible(True)
            self.label_img3.setVisible(True), self.load_img3.setVisible(True)
            self.label_img4.setVisible(True), self.load_img4.setVisible(True)
        else:
            self.label_img2.setVisible(False), self.load_img2.setVisible(False)
            self.label_img3.setVisible(False), self.load_img3.setVisible(False)
            self.label_img4.setVisible(False), self.load_img4.setVisible(False)
            self.label_img3.clear(), self.label_img4.clear(), self.label_img2.clear()

    def resized_image(self, src, w, h):
        resize_image = cv2.resize(src, (int(w), int(h)), interpolation=cv2.INTER_CUBIC)
        return resize_image

    def showall(self):
        global b
        try:
            h1, w1, c1 = self.imageTemp.shape
            img2 = cv2.imread(self.img2)
            h2, w2, c2 = img2.shape
            arr = []  # create empty list
            if self.count_cbox.currentText() == "2":
                if self.merge_cbox.currentText() == "Horizontal":
                    self.axis = 1
                    if h1 >= h2:
                        factor = h1 / h2
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, w2 * factor, h2 * factor))

                    elif h2 >= h1:
                        factor = h2 / h1
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2, h2))
                elif self.merge_cbox.currentText() == "Vertical":
                    self.axis = 0
                    if w1 >= w2:
                        factor = w1 / w2
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, w2 * factor, h2 * factor))

                    elif w2 >= w1:
                        factor = w2 / w1
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2, h2))
            elif self.count_cbox.currentText() == "3":
                img3 = cv2.imread(self.img3)
                h3, w3, c3 = img3.shape
                if self.merge_cbox.currentText() == "Horizontal":
                    self.axis = 1
                    if h1 >= h2 and h1 >= h3:
                        factor = h1 / h2
                        factor2 = h1 / h3
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, w2 * factor, h2 * factor))
                        arr.append(self.resized_image(img3, w3 * factor2, h3 * factor2))

                    elif h2 >= h1 and h2 >= h3:
                        factor = h2 / h1
                        factor2 = h2 / h3
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2, h2))
                        arr.append(self.resized_image(img3, w3 * factor2, h3 * factor2))
                    else:
                        factor = h3 / h1
                        factor2 = h3 / h2
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2 * factor2, h2 * factor2))
                        arr.append(self.resized_image(img3, w3, h3))
                elif self.merge_cbox.currentText() == "Vertical":
                    self.axis = 0
                    if w1 >= w2 and w1 >= w3:
                        factor = w1 / w2
                        factor2 = w1 / w3
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, w2 * factor, h2 * factor))
                        arr.append(self.resized_image(img3, w3 * factor2, h3 * factor2))

                    elif w2 >= w1 and w2 >= w3:
                        factor = w2 / w1
                        factor2 = w2 / w3
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2, h2))
                        arr.append(self.resized_image(img3, w3 * factor2, h3 * factor2))
                    else:
                        factor = w3 / w1
                        factor2 = w3 / w2
                        arr.append(self.resized_image(self.imageTemp, w1 * factor, h1 * factor))
                        arr.append(self.resized_image(img2, w2 * factor2, h2 * factor2))
                        arr.append(self.resized_image(img3, w3, h3))
            elif self.count_cbox.currentText() == "4":
                img3 = cv2.imread(self.img3)
                h3, w3, c3 = img3.shape
                img4 = cv2.imread(self.img4)
                h4, w4, c4 = img4.shape
                if self.merge_cbox.currentText() == "Horizontal":
                    self.axis = 1
                    if h1 >= h2 and h1 >= h3 and h1 >= h4:
                        factor = h1 / h2
                        factor2 = h1 / h3
                        factor3 = h1 / h4
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))
                        arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))

                    elif h2 >= h1 and h2 >= h3 and h2 >= h4:
                        factor = h2 / h1
                        factor2 = h2 / h3
                        factor3 = h2 / h4
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, w2, h2))
                        arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))
                    elif h3 >= h1 and h3 >= h2 and h3 >= h4:
                        factor = h3 / h1
                        factor2 = h3 / h2
                        factor3 = h3 / h4
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                        arr.append(self.resized_image(img3, w3, h3))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))
                    else:
                        factor = h4 / h1
                        factor2 = h4 / h2
                        factor3 = h4 / h3
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                        arr.append(self.resized_image(img3, int(w3 * factor3), int(h3 * factor3)))
                        arr.append(self.resized_image(img4, w4, h4))
                elif self.merge_cbox.currentText() == "Vertical":
                    self.axis = 0
                    if w1 >= w2 and w1 >= w3 and w1 >= w4:
                        factor = w1 / w2
                        factor2 = w1 / w3
                        factor3 = w1 / w4
                        arr.append(self.resized_image(self.imageTemp, w1, h1))
                        arr.append(self.resized_image(img2, int(w2 * factor), int(h2 * factor)))
                        arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))

                    elif w2 >= w1 and w2 >= w3 and w2 >= w4:
                        factor = w2 / w1
                        factor2 = w2 / w3
                        factor3 = w2 / w4
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, w2, h2))
                        arr.append(self.resized_image(img3, int(w3 * factor2), int(h3 * factor2)))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))
                    elif w3 >= w1 and w3 >= w2 and w3 >= w4:
                        factor = w3 / w1
                        factor2 = w3 / w2
                        factor3 = w3 / w4
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                        arr.append(self.resized_image(img3, w3, h3))
                        arr.append(self.resized_image(img4, int(w4 * factor3), int(h4 * factor3)))
                    else:
                        factor = w4 / w1
                        factor2 = w4 / w2
                        factor3 = w4 / w3
                        arr.append(self.resized_image(self.imageTemp, int(w1 * factor), int(h1 * factor)))
                        arr.append(self.resized_image(img2, int(w2 * factor2), int(h2 * factor2)))
                        arr.append(self.resized_image(img3, int(w3 * factor3), int(h3 * factor3)))
                        arr.append(self.resized_image(img4, w4, h4))

            # merge and display image
            for i in enumerate(arr):
                b = np.concatenate((arr), axis=self.axis)
                self.checkImage(b)
                self.displayImage(b)
        except:
            self.error()

    def getDilationSliderValue(self):
        self.label_dilationKernel.setText("kernel = ("+str(self.dilation_slider.value())+" , "+str(self.dilation_slider.value())+")")

    def getDilateKernel(self):
        kernel = np.ones((int(self.dilation_slider.value()), int(self.dilation_slider.value())), np.uint8)
        return kernel

    def dilationClicked(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2GRAY)
        canny = cv2.Canny(gray, 100, 200)
        b = cv2.dilate(canny, self.getDilateKernel(), iterations=1)
        self.checkImage(b)
        self.displayImage(b)

    def getErosionSliderValue(self):
        self.label_erosionKernel.setText("kernel = ("+str(self.erosion_slider.value())+" , "+str(self.erosion_slider.value())+")")

    def getErodeKernel(self):
        kernel = np.ones((int(self.erosion_slider.value()), int(self.erosion_slider.value())), np.uint8)
        return kernel

    def erosionClicked(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_RGB2GRAY)
        canny = cv2.Canny(gray, 100, 200)
        dilation = cv2.dilate(canny, self.getErodeKernel(), iterations=1)
        b = cv2.erode(dilation, self.getErodeKernel(), iterations=1)
        self.checkImage(b)
        self.displayImage(b)

    def cannyEdge(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
        b = cv2.Canny(gray, 100, 200)
        self.checkImage(b)
        self.displayImage(b)

    def sobelEdge(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=5)
        b = sobelx + sobely
        self.checkImage(b)
        self.displayImage(b)

    def prewittEdge(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        img_prewittx = cv2.filter2D(gray, -1, kernelx)
        img_prewitty = cv2.filter2D(gray, -1, kernely)
        b = img_prewittx + img_prewitty
        self.checkImage(b)
        self.displayImage(b)

    def imgToHafltone(self):
        global b
        gray = cv2.cvtColor(self.imageTemp, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape
        b = np.zeros((2 * height, 2 * width)).astype(np.uint8)
        dict = {0: [[0, 0], [0, 0]],
                51: [[255, 0], [0, 0]],
                102: [[0, 255], [255, 0]],
                153: [[255, 255], [255, 0]],
                204: [[255, 255], [255, 255]]}

        for row in range(height):
            for col in range(width):
                val = gray[row][col]
                if (val > 204):
                    b[row * 2:row * 2 + 2, col * 2:col * 2 + 2] = dict[204]
                elif (val > 153):
                    b[row * 2:row * 2 + 2, col * 2:col * 2 + 2] = dict[153]
                elif (val > 102):
                    b[row * 2:row * 2 + 2, col * 2:col * 2 + 2] = dict[102]
                elif (val > 51):
                    b[row * 2:row * 2 + 2, col * 2:col * 2 + 2] = dict[51]
                else:
                    b[row * 2:row * 2 + 2, col * 2:col * 2 + 2] = dict[0]
        self.checkImage(b)
        self.displayImage(b)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())

