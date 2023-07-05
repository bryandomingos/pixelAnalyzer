from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
from pymsgbox import alert
from pynput.mouse import Listener
from tkinter import *


class Ui_Dialog(object):

    def clickStart(self):
        print("teste")

        alert(text='Clique no pixel a ser analizado', title='Selecione um Pixel', button='OK')

        def on_click(j, k, button, pressed):
            if pressed:
                print('Mouse clicked at ({0}, {1}) with {2}'.format(j, k, button))
            if not pressed:
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        x, y = pyautogui.position()
        r1, g1, b1 = pyautogui.pixel(x, y)

        global run
        run = True

        while run:
            r, g, b = pyautogui.pixel(x, y)
            rgb = (r, g, b)
            if rgb == (r1, g1, b1):
                Dialog.update()
                print("RGB: ", r, g, b, "XY: ", x, y)
            elif rgb != (r1, g1, b1):
                print("Alerta de cor")

    def clickStop(self):
        global run
        run = False

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(281, 122)
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.start.setObjectName("start")
        self.start.clicked.connect(self.clickStart)
        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.stop.setObjectName("stop")
        self.radioMouse = QtWidgets.QRadioButton(Dialog)
        self.radioMouse.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioMouse.setObjectName("radioMouse")
        self.radioKeyboard = QtWidgets.QRadioButton(Dialog)
        self.radioKeyboard.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.radioKeyboard.setObjectName("radioKeyboard")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 20, 171, 91))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start.setText(_translate("Dialog", "Start"))
        self.stop.setText(_translate("Dialog", "Stop"))
        self.radioMouse.setText(_translate("Dialog", "Mouse"))
        self.radioKeyboard.setText(_translate("Dialog", "Keyboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
