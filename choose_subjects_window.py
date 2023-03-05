from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QLabel
import sys

subjects = ["Differential Equations and Transforms",
            "Structured and Object Oriented Programming",
            "Technical English Communication",
            "Engineering Physics",
            "Data Structure and Algorithms",
            "Quantitative Skills I"]

class ChooseSubjectsWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_subjects = set()

        self.setWindowTitle("Better FFCS")

        self.setLayout(QtWidgets.QGridLayout())

        self.choose_subjects_label()
        self.show_subjects()
        self.next_button()

        # self.show()

    def show_subjects(self):
        self.subject_options = []

        for i in range(len(subjects)):
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
                self.selected_subjects.add(subjects[i])

        print(self.selected_subjects)

    def choose_subjects_label(self):
        label = QLabel("Choose your subjects\n")

        self.layout().addWidget(label)


app = QApplication(sys.argv)
subjects_window = ChooseSubjectsWindow()
sys.exit(app.exec_())

