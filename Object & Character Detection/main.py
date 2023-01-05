from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import sys, cv2

from gui import Ui_MainWindow
import size as s
import size_sobel as ss
import size_prewitt as sp
import characterDetection as cd
import thinning as tt

input_image=""
b=""

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

#*************button_behaviour******************************
        self.actionLoad.triggered.connect(self.loadImage)
        self.actionSave.triggered.connect(self.saveImage)
        self.actionExit.triggered.connect(self.closeApp)
        self.b_detect.clicked.connect(self.detectCharacter)
        self.b_thinning.clicked.connect(self.thinning_output)
        self.pushButton.clicked.connect(self.loadMeasure)

    def loadImage(self, MainWindow):
        global input_image
        input_image = QtWidgets.QFileDialog.getOpenFileName(self, 'select image', 'D:\\')[0]
        pixmap = QtGui.QPixmap(input_image)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.show_image.setPixmap(scaledImage)

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
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No image to save")
            msg.setWindowTitle("ERROR!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def closeApp(self):
        msg = QtWidgets.QMessageBox.question(self, 'Exit Confirmation', "Are you want to Quit?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            return

    def displayImage(self, b):
        if len(b.shape) == 3:
            c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        else:
            c = QtGui.QImage(b, b.shape[1], b.shape[0], b.shape[1], QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(c)
        scaledImage = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.show_image.setPixmap(scaledImage)

    def loadMeasure(self):
        global b
        if self.comboBox.currentText()=="Using Canny":
            b = s.getImage(input_image)
        elif self.comboBox.currentText()=="Using Sobel":
            b = ss.getImage(input_image)
        elif self.comboBox.currentText()=="Using Prewitt":
            b = sp.getImage(input_image)
        self.displayImage(b)


    def detectCharacter(self):
        global b
        # input_image2 = cv2.imread(input_image)
        # gray = cv2.cvtColor(input_image2, cv2.COLOR_BGR2GRAY)
        # ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        # kernel = np.ones((10, 1), np.uint8)
        # img_dilation = cv2.dilate(thresh, kernel, iterations=1)
        # cv2MajorVersion = cv2.__version__.split(".")[0]
        # if int(cv2MajorVersion) >= 4:
        #     ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # else:
        #     im2, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #
        # sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
        # for i, ctr in enumerate(sorted_ctrs):
        #     x, y, w, h = cv2.boundingRect(ctr)
        #     roi = input_image2[y:y + h, x:x + w]
        #     cv2.rectangle(input_image2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #
        # self.displayImage(input_image2)
        b = cd.getImage(input_image)
        self.displayImage(b)

    def thinning_output(self):
        global b
        a = cv2.imread(input_image, 0)
        b = tt.fastThin(a)
        self.displayImage(b)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
