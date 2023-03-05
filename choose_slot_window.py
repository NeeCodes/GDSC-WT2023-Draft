from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QLabel
import sys

# from choose_subjects_window import ChooseSubjectsWindow
# import choose_subjects_window

class ChooseSlotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.next_window = QMainWindow()

        self.selected_slot = -1

        self.setWindowTitle("Better FFCS")

        self.setLayout(QtWidgets.QGridLayout())

        self.choose_slot_label()
        self.show_slots()
        self.next_button()

        self.show()

    def show_slots(self):
        self.morning_theory = QRadioButton()
        self.morning_theory.setText("Morning Theory / Evening Labs")

        self.evening_theory = QRadioButton()
        self.evening_theory.setText("Evening Theory / Morning Labs")


        self.layout().addWidget(self.morning_theory)
        self.layout().addWidget(self.evening_theory)

    def next_button(self):
        next_button = QPushButton(clicked = lambda: self.next_button_clicked())
        # next_button.clicked.connect(self.next_button_clicked)

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
        label = QLabel("Choose your preferred slot\n")

        self.layout().addWidget(label)


app = QApplication(sys.argv)

style = """QWidget {
    background-color: "#2C3333";
    color: "#ffffff";
}"""

app.setStyleSheet(style)

slot_window = ChooseSlotWindow()
sys.exit(app.exec_())

