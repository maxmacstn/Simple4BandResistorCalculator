import sys
from PyQt5 import QtGui

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from MainWindowGUI import Ui_MainWindow


class ResistorCalcGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.digitColorList = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
        self.multiplierColorList = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gold", "grey"]
        self.toleranceColorList = ["brown", "red", "gold", "grey"]

        self.num = 0
        self.firstDigitCombobox = self.ui.firstComboBox
        self.secondDigitCombobox = self.ui.secondComboBox
        self.multiplierCombobox = self.ui.secondComboBox_2
        self.toleranceCombobox = self.ui.secondComboBox_3

        self.firstDigitCombobox.currentIndexChanged.connect(self.updateValue)
        self.secondDigitCombobox.currentIndexChanged.connect(self.updateValue)
        self.multiplierCombobox.currentIndexChanged.connect(self.updateValue)
        self.toleranceCombobox.currentIndexChanged.connect(self.updateValue)

        self.ui.pushButton.pressed.connect(self.reset)

        self.paintComboboxColor()

        self.reset()
        self.updateValue()

    def paintComboboxColor(self):
        model1 = self.firstDigitCombobox.model()
        model2 = self.secondDigitCombobox.model()
        model3 = self.multiplierCombobox.model()
        model4 = self.toleranceCombobox.model()

        for row in range(9):
            if (row in [0,1,5,6,8]):
                model1.item(row).setForeground(QtGui.QColor("white"))
                model2.item(row).setForeground(QtGui.QColor("white"))
            model1.item(row).setBackground(QtGui.QColor(self.digitColorList[row]))
            model2.item(row).setBackground(QtGui.QColor(self.digitColorList[row]))

        for row in range(10):
            if (row in [0,1,5,6,9]):
                model3.item(row).setForeground(QtGui.QColor("white"))
            model3.item(row).setBackground(QtGui.QColor(self.multiplierColorList[row]))

        for row in range(4):
            if (row in [0,3]):
                model4.item(row).setForeground(QtGui.QColor("white"))
            model4.item(row).setBackground(QtGui.QColor(self.toleranceColorList[row]))




    def updateValue(self):
        resistorValue = self.firstDigitCombobox.currentIndex() * 100
        resistorValue += self.secondDigitCombobox.currentIndex() * 10

        if (int(self.multiplierCombobox.currentIndex()) <= 7):
            resistorValue *= pow(10, int(self.multiplierCombobox.currentIndex()))
        else:
            if (int(self.multiplierCombobox.currentIndex() == 8)):
                resistorValue *= 0.1
            if (int(self.multiplierCombobox.currentIndex() == 9)):
                resistorValue *= 0.01

        toleranceList = [1, 2, 5, 10]
        tolerance = "±" + str(toleranceList[self.toleranceCombobox.currentIndex()]) + "%"

        output = str(self.human_format(resistorValue)) + "Ω  " + tolerance

        self.ui.firstDigitLabel.setStyleSheet("background-color:"+self.digitColorList[self.firstDigitCombobox.currentIndex()]+";")
        self.ui.secondDigitLabel.setStyleSheet("background-color:"+self.digitColorList[self.secondDigitCombobox.currentIndex()]+";")
        self.ui.miltiplierDigitLabel_3.setStyleSheet("background-color:"+self.multiplierColorList[self.multiplierCombobox.currentIndex()]+";")
        self.ui.tolerenceDigitLabel.setStyleSheet("background-color:"+self.toleranceColorList[self.toleranceCombobox.currentIndex()]+";")
        self.ui.resultLineEdit.setText(output)

    def human_format(self, num):
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '%.1f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

    def reset(self):
        self.firstDigitCombobox.setCurrentIndex(0)
        self.secondDigitCombobox.setCurrentIndex(0)
        self.multiplierCombobox.setCurrentIndex(0)
        self.toleranceCombobox.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ResistorCalcGUI()
    w.show()
    sys.exit(app.exec_())
