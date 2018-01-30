# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 540)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.resistor_plain = QtWidgets.QLabel(self.centralwidget)
        self.resistor_plain.setGeometry(QtCore.QRect(110, 110, 501, 191))
        self.resistor_plain.setObjectName("resistor_plain")
        self.resistor_mask = QtWidgets.QLabel(self.centralwidget)
        self.resistor_mask.setGeometry(QtCore.QRect(110, 110, 501, 191))
        self.resistor_mask.setAutoFillBackground(False)
        self.resistor_mask.setStyleSheet("background-color: transparent;")
        self.resistor_mask.setText("")
        self.resistor_mask.setPixmap(QtGui.QPixmap("asset/resistor_mask.png"))
        self.resistor_mask.setScaledContents(False)
        self.resistor_mask.setObjectName("resistor_mask")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 300, 411, 77))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.secondComboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.secondComboBox_2.setObjectName("secondComboBox_2")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.secondComboBox_2.addItem("")
        self.gridLayout.addWidget(self.secondComboBox_2, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.firstComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.firstComboBox.setObjectName("firstComboBox")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.firstComboBox.addItem("")
        self.gridLayout.addWidget(self.firstComboBox, 1, 0, 1, 1)
        self.secondComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.secondComboBox.setObjectName("secondComboBox")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.secondComboBox.addItem("")
        self.gridLayout.addWidget(self.secondComboBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.secondComboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.secondComboBox_3.setObjectName("secondComboBox_3")
        self.secondComboBox_3.addItem("")
        self.secondComboBox_3.addItem("")
        self.secondComboBox_3.addItem("")
        self.secondComboBox_3.addItem("")
        self.gridLayout.addWidget(self.secondComboBox_3, 1, 5, 1, 1)
        self.firstDigitLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstDigitLabel.setGeometry(QtCore.QRect(290, 120, 21, 81))
        self.firstDigitLabel.setStyleSheet("background-color: brown;")
        self.firstDigitLabel.setText("")
        self.firstDigitLabel.setObjectName("firstDigitLabel")
        self.secondDigitLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondDigitLabel.setGeometry(QtCore.QRect(320, 120, 16, 81))
        self.secondDigitLabel.setStyleSheet("background-color: brown;")
        self.secondDigitLabel.setText("")
        self.secondDigitLabel.setObjectName("secondDigitLabel")
        self.miltiplierDigitLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.miltiplierDigitLabel_3.setGeometry(QtCore.QRect(350, 120, 16, 81))
        self.miltiplierDigitLabel_3.setStyleSheet("background-color: brown;")
        self.miltiplierDigitLabel_3.setText("")
        self.miltiplierDigitLabel_3.setObjectName("miltiplierDigitLabel_3")
        self.tolerenceDigitLabel = QtWidgets.QLabel(self.centralwidget)
        self.tolerenceDigitLabel.setGeometry(QtCore.QRect(390, 120, 21, 81))
        self.tolerenceDigitLabel.setStyleSheet("background-color: brown;")
        self.tolerenceDigitLabel.setText("")
        self.tolerenceDigitLabel.setObjectName("tolerenceDigitLabel")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 430, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.resultLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resultLineEdit.setGeometry(QtCore.QRect(280, 430, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resultLineEdit.setFont(font)
        self.resultLineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.resultLineEdit.setText("")
        self.resultLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultLineEdit.setReadOnly(True)
        self.resultLineEdit.setObjectName("resultLineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 430, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.resistor_plain.raise_()
        self.gridLayoutWidget.raise_()
        self.firstDigitLabel.raise_()
        self.secondDigitLabel.raise_()
        self.miltiplierDigitLabel_3.raise_()
        self.tolerenceDigitLabel.raise_()
        self.resistor_mask.raise_()
        self.label_6.raise_()
        self.resultLineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ResistorCalc"))
        self.label.setText(_translate("MainWindow", "4-Band Resistor Color Code Calculator"))
        self.resistor_plain.setPixmap(QtGui.QPixmap("asset/resistor_plain.png"))
        self.label_4.setText(_translate("MainWindow", "Multiplier:"))
        self.secondComboBox_2.setItemText(0, _translate("MainWindow", "BLACK"))
        self.secondComboBox_2.setItemText(1, _translate("MainWindow", "BROWN"))
        self.secondComboBox_2.setItemText(2, _translate("MainWindow", "RED"))
        self.secondComboBox_2.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.secondComboBox_2.setItemText(4, _translate("MainWindow", "YELLOW"))
        self.secondComboBox_2.setItemText(5, _translate("MainWindow", "GREEN"))
        self.secondComboBox_2.setItemText(6, _translate("MainWindow", "BLUE"))
        self.secondComboBox_2.setItemText(7, _translate("MainWindow", "VIOLET"))
        self.secondComboBox_2.setItemText(8, _translate("MainWindow", "GOLD"))
        self.secondComboBox_2.setItemText(9, _translate("MainWindow", "SLIVER"))
        self.label_2.setText(_translate("MainWindow", "1st Digit:"))
        self.label_3.setText(_translate("MainWindow", "2nd Digit:"))
        self.firstComboBox.setItemText(0, _translate("MainWindow", "BLACK"))
        self.firstComboBox.setItemText(1, _translate("MainWindow", "BROWN"))
        self.firstComboBox.setItemText(2, _translate("MainWindow", "RED"))
        self.firstComboBox.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.firstComboBox.setItemText(4, _translate("MainWindow", "YELLOW"))
        self.firstComboBox.setItemText(5, _translate("MainWindow", "GREEN"))
        self.firstComboBox.setItemText(6, _translate("MainWindow", "BLUE"))
        self.firstComboBox.setItemText(7, _translate("MainWindow", "VIOLET"))
        self.firstComboBox.setItemText(8, _translate("MainWindow", "GREY"))
        self.firstComboBox.setItemText(9, _translate("MainWindow", "WHITE"))
        self.secondComboBox.setItemText(0, _translate("MainWindow", "BLACK"))
        self.secondComboBox.setItemText(1, _translate("MainWindow", "BROWN"))
        self.secondComboBox.setItemText(2, _translate("MainWindow", "RED"))
        self.secondComboBox.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.secondComboBox.setItemText(4, _translate("MainWindow", "YELLOW"))
        self.secondComboBox.setItemText(5, _translate("MainWindow", "GREEN"))
        self.secondComboBox.setItemText(6, _translate("MainWindow", "BLUE"))
        self.secondComboBox.setItemText(7, _translate("MainWindow", "VIOLET"))
        self.secondComboBox.setItemText(8, _translate("MainWindow", "GREY"))
        self.secondComboBox.setItemText(9, _translate("MainWindow", "WHITE"))
        self.label_5.setText(_translate("MainWindow", "Tolerence:"))
        self.secondComboBox_3.setItemText(0, _translate("MainWindow", "BROWN"))
        self.secondComboBox_3.setItemText(1, _translate("MainWindow", "RED"))
        self.secondComboBox_3.setItemText(2, _translate("MainWindow", "GOLD"))
        self.secondComboBox_3.setItemText(3, _translate("MainWindow", "SLIVER"))
        self.label_6.setText(_translate("MainWindow", "Resistor value:"))
        self.pushButton.setText(_translate("MainWindow", "Reset"))
