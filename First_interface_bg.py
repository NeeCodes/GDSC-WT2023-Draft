from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# from choose_subjects_window import ChooseSubjectsWindow
# import choose_subjects_window

class ChooseSlotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.next_window = QMainWindow()

        self.selected_slot = -1

        self.setWindowTitle("Better FFCS")
        self.setGeometry(100, 100, 540, 540)
        self.setLayout(QtWidgets.QGridLayout())
        self.label1 = QLabel(self)
        self.label1.resize(540, 540)
        self.label1.setStyleSheet("background-image:url(C:/Users/WELCOME/Downloads/WhatsApp Image 2023-03-05 at 08.26.53 (1).jpeg);border: 1px blue")
        self.choose_slot_label()
        self.show_slots()
        self.next_button()
        self.show()

    def show_slots(self):
        self.morning_theory = QRadioButton()
        self.morning_theory.setText("Morning Theory / Evening Labs")
        self.morning_theory.setFont(QFont('Arial',15))
        self.morning_theory.setStyleSheet("background-color:rgba(255,255,255,10)")
        self.evening_theory = QRadioButton()
        self.evening_theory.setText("Evening Theory / Morning Labs")
        self.evening_theory.setFont(QFont('Arial',15))
        self.evening_theory.setStyleSheet("background-color:rgba(255,255,255,10)")


        self.layout().addWidget(self.morning_theory)
        self.layout().addWidget(self.evening_theory)

    def next_button(self):
        next_button = QPushButton("Next",clicked = lambda: self.next_button_clicked())
        next_button.setStyleSheet("background-color:rgba(255,255,255,10)")
        next_button.clicked.connect(self.next_button_clicked)
        self.layout().addWidget(next_button)


    def next_button_clicked(self):
        if self.morning_theory.isChecked():
            self.selected_slot = 0
            print("Morning theory")
        else:
            self.selected_slot = 1
            print("Morning Labs")

        # go to the next window
        # self.next_window = choose_subjects_window.ChooseSubjectsWindow()
        # self.next_window.show()

    def choose_slot_label(self):
        label2 = QLabel("Choose your preferred slot")
        label2.setFont(QFont('Arial',15))
        label2.setGeometry(10, 10, 10, 10)
        label2.resize(10,10)
        self.layout().addWidget(label2)
        label2.setStyleSheet("background-color:rgba(255,255,255,10)")

app = QApplication(sys.argv)

style = """QWidget {
    background-color: "#2C3333";
    color: "#ffffff";
}"""

app.setStyleSheet(style)

slot_window = ChooseSlotWindow()
sys.exit(app.exec_())