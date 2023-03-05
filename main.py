from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import pandas as pd
import sys
import os

dir = os.getcwd()
path = dir+"/bg.jpeg"
# background-image: url(/home/nee/Desktop/Code/Python/gdscwt2023/bg.jpeg);

selected_subjects = []

# ffcs_list = []


class ChooseSlotWindow(QtWidgets.QWidget):

    selected_slot = -1

    def __init__(self):
        super().__init__()

        # self.next_window = window

        # self.selected_slot = -1

        self.setWindowTitle("Better FFCS")

        self.setLayout(QtWidgets.QGridLayout())


        self.choose_slot_label()
        self.show_slots()
        self.next_button()

        # self.show()

    def set_next_window(self, window):
        self.next_window = window

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
        global ffcs_list

        if self.morning_theory.isChecked():
            self.selected_slot = 0
            # global ffcs_list
            ffcs_list = pd.read_excel('data!!.xlsx', sheet_name = 'Morning slot')

        else:
            self.selected_slot = 1
            # global ffcs_list
            ffcs_list = pd.read_excel('data!!.xlsx', sheet_name = 'Evening slot')

        global subjects
        subjects = ffcs_list.subjects.unique()

        # go to the next window
        # self.next_window = choose_subjects_window.ChooseSubjectsWindow()
        # self.next_window.show()

    def choose_slot_label(self):
        label = QLabel("Choose your preferred slot\n")

        self.layout().addWidget(label)





class ChooseSubjectsWindow(QtWidgets.QWidget):

    def __init__(self, subjects):
        super().__init__()

        self.subjects = subjects

        self.setWindowTitle("Better FFCS")

        self.setLayout(QtWidgets.QGridLayout())

        self.choose_subjects_label()
        self.show_subjects()
        self.next_button()

        # self.show()

    def show_subjects(self):
        self.subject_options = []

        for i in range(len(self.subjects)):
            temp = QCheckBox()
            self.subject_options.append(temp)

            self.subject_options[i].setObjectName(f"subject{i}")
            self.subject_options[i].setText(f"{subjects[i]}")

            self.layout().addWidget(self.subject_options[i])

    def next_button(self):
        next_button = QPushButton()
        next_button.clicked.connect(self.next_button_clicked)

        self.layout().addWidget(next_button)

    def next_button_clicked(self):
        for i in range(len(self.subject_options)):
            if self.subject_options[i].isChecked():
                selected_subjects.add(subjects[i])

        print(selected_subjects)

    def choose_subjects_label(self):
        label = QLabel("Choose your subjects\n")

        self.layout().addWidget(label)


app = QApplication(sys.argv)

style = """QWidget {
    background-color: #191825;
    color: "#ffffff";
    
}"""

app.setStyleSheet(style)

slot_window = ChooseSlotWindow()
slot_window.show()
subjects_window = ChooseSubjectsWindow()

slot_window.set_next_window(subjects_window)





sys.exit(app.exec_())

