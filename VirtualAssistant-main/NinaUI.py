


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circle = QtWidgets.QLabel(self.centralwidget)
        self.circle.setGeometry(QtCore.QRect(0, 0, 591, 460))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.circle.setFont(font)
        self.circle.setStyleSheet("font: 8pt \"Roman\";\n" "z-index: 2;")
        self.circle.setText("")
        self.circle.setPixmap(QtGui.QPixmap("img/LCPT.gif"))
        self.circle.setScaledContents(True)
        self.circle.setIndent(-1)
        self.circle.setObjectName("circle")


        self.circle2 = QtWidgets.QLabel(self.centralwidget)
        self.circle2.setGeometry(QtCore.QRect(0, 0, 591, 460))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.circle2.setFont(font)
        self.circle2.setStyleSheet("font: 8pt \"Roman\";\n" "z-index: 2;")
        self.circle2.setText("")
        self.circle2.setPixmap(QtGui.QPixmap("img/LCPT.gif"))
        self.circle2.setScaledContents(True)
        self.circle2.setIndent(-1)
        self.circle2.setObjectName("circle")

        self.Say = QtWidgets.QPushButton(self.centralwidget)
        self.Say.setGeometry(QtCore.QRect(255, 227, 101, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.Say.setFont(font)
        self.Say.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(18, 4, 33);\n"
"\n"
"background-color: rgb(18, 4, 33);\n"
"border-color: rgb(205, 169, 244);\n"
"border-color: rgb(205, 169, 244);\n")
        self.Say.setCheckable(False)
        self.Say.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nina"))
        self.Say.setText(_translate("MainWindow", "N.I.N.A"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
