from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi2(self)

    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 491)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 170, 127, 255), stop:1 rgba(170, 170, 127, 255));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 631, 491))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.raise_()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Simple Photo Editor</p><p align=\"right\"><span style=\" color:#005500; vertical-align:sub;\">2019.2</span></p><p align=\"center\"><span style=\" font-size:8pt; color:#141414;\">This application is design using Qt Designer and Jetbrains Pycharm Community 2018.3</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:400; color:#060606;\">It is a user friendly application that even a beginner can use!</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:400; color:#060606;\">The application promise you a simple yet an interesting filter and effect for your picture to make ur beautiful picture become more beautiful! </span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:400; color:#060606;\">please do save ur picture before exit ya :) Enjoy your day and have fun with the application!</span></p><p align=\"center\"><span style=\" font-size:9pt; color:#00007f;\">Developed by: </span></p><p align=\"center\"><span style=\" font-size:9pt; color:#00007f;\">Sahdan Chung BS17160646</span></p><p align=\"center\"><span style=\" font-size:9pt; color:#00007f;\">Ninie Racha Anak Anding BS17160687</span></p></body></html>"))

if __name__ == "__main__":
    window = QtWidgets.QApplication(sys.argv)
    Dialog= QtWidgets.QDialog()
    ex = Ui_Dialog()
    ex.setupUi2(Dialog)
    ex.show()
    sys.exit(window.exec_())
