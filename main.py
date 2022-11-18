from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 220, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Push me to make a Circle"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class FirstForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(FirstForm, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_Circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_Circle(self, qp):
        qp.setBrush(QColor(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
        radius = random.randint(10, 60)
        qp.drawEllipse(random.randint(0, self.width()), random.randint(0, self.height()), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
