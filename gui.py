# Form implementation generated from reading ui file '.\calculator.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 500)
        MainWindow.setMaximumSize(QtCore.QSize(580, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.top_label.setGeometry(QtCore.QRect(250, 10, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.ans_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ans_label.setGeometry(QtCore.QRect(200, 70, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ans_label.setFont(font)
        self.ans_label.setText("")
        self.ans_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ans_label.setObjectName("ans_label")
        self.push_seven = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_seven.setGeometry(QtCore.QRect(60, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_seven.setFont(font)
        self.push_seven.setObjectName("push_seven")
        self.push_four = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_four.setGeometry(QtCore.QRect(60, 260, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_four.setFont(font)
        self.push_four.setObjectName("push_four")
        self.push_one = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_one.setGeometry(QtCore.QRect(60, 320, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_one.setFont(font)
        self.push_one.setObjectName("push_one")
        self.push_eight = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_eight.setGeometry(QtCore.QRect(180, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_eight.setFont(font)
        self.push_eight.setObjectName("push_eight")
        self.push_five = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_five.setGeometry(QtCore.QRect(180, 260, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_five.setFont(font)
        self.push_five.setObjectName("push_five")
        self.push_two = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_two.setGeometry(QtCore.QRect(180, 320, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_two.setFont(font)
        self.push_two.setObjectName("push_two")
        self.push_nine = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_nine.setGeometry(QtCore.QRect(300, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_nine.setFont(font)
        self.push_nine.setObjectName("push_nine")
        self.push_six = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_six.setGeometry(QtCore.QRect(300, 260, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_six.setFont(font)
        self.push_six.setObjectName("push_six")
        self.push_three = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_three.setGeometry(QtCore.QRect(300, 320, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_three.setFont(font)
        self.push_three.setObjectName("push_three")
        self.push_divide = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_divide.setGeometry(QtCore.QRect(420, 140, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_divide.setFont(font)
        self.push_divide.setObjectName("push_divide")
        self.push_multiply = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_multiply.setGeometry(QtCore.QRect(420, 200, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_multiply.setFont(font)
        self.push_multiply.setObjectName("push_multiply")
        self.push_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_minus.setGeometry(QtCore.QRect(420, 260, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_minus.setFont(font)
        self.push_minus.setObjectName("push_minus")
        self.push_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_add.setGeometry(QtCore.QRect(420, 320, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_add.setFont(font)
        self.push_add.setObjectName("push_add")
        self.push_zero = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_zero.setGeometry(QtCore.QRect(180, 380, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_zero.setFont(font)
        self.push_zero.setObjectName("push_zero")
        self.push_decimal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_decimal.setGeometry(QtCore.QRect(300, 380, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.push_decimal.setFont(font)
        self.push_decimal.setObjectName("push_decimal")
        self.push_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_submit.setGeometry(QtCore.QRect(420, 380, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_submit.setFont(font)
        self.push_submit.setObjectName("push_submit")
        self.push_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_clear.setGeometry(QtCore.QRect(60, 140, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_clear.setFont(font)
        self.push_clear.setObjectName("push_clear")
        self.push_negative = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_negative.setGeometry(QtCore.QRect(180, 140, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_negative.setFont(font)
        self.push_negative.setObjectName("push_negative")
        self.push_percentage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_percentage.setGeometry(QtCore.QRect(300, 140, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_percentage.setFont(font)
        self.push_percentage.setObjectName("push_percentage")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(80, 380, 60, 60))
        self.logo.setStyleSheet("background-image:url(:/uno/logo_uno.png)")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo_uno.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.historyButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.historyButton.setGeometry(QtCore.QRect(460, 10, 113, 32))
        self.historyButton.setObjectName("historyButton")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(650, 50, 200, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 348))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.historyLabel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.historyLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyLabel.sizePolicy().hasHeightForWidth())
        self.historyLabel.setSizePolicy(sizePolicy)
        self.historyLabel.setText("")
        self.historyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.historyLabel.setObjectName("historyLabel")
        self.verticalLayout.addWidget(self.historyLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.top_label.setText(_translate("MainWindow", "Calculator"))
        self.push_seven.setText(_translate("MainWindow", "7"))
        self.push_four.setText(_translate("MainWindow", "4"))
        self.push_one.setText(_translate("MainWindow", "1"))
        self.push_eight.setText(_translate("MainWindow", "8"))
        self.push_five.setText(_translate("MainWindow", "5"))
        self.push_two.setText(_translate("MainWindow", "2"))
        self.push_nine.setText(_translate("MainWindow", "9"))
        self.push_six.setText(_translate("MainWindow", "6"))
        self.push_three.setText(_translate("MainWindow", "3"))
        self.push_divide.setText(_translate("MainWindow", "÷"))
        self.push_multiply.setText(_translate("MainWindow", "×"))
        self.push_minus.setText(_translate("MainWindow", "-"))
        self.push_add.setText(_translate("MainWindow", "+"))
        self.push_zero.setText(_translate("MainWindow", "0"))
        self.push_decimal.setText(_translate("MainWindow", "."))
        self.push_submit.setText(_translate("MainWindow", "="))
        self.push_clear.setText(_translate("MainWindow", "A/C"))
        self.push_negative.setText(_translate("MainWindow", "+/-"))
        self.push_percentage.setText(_translate("MainWindow", "%"))
        self.historyButton.setText(_translate("MainWindow", "History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
