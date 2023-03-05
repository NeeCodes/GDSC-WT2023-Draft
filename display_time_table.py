from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QLabel
import sys

class DisplayTimetables(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.theory = [[0 for i in range(5)] for j in range(5)]
        self.labs = [[0 for i in range(5)] for j in range(5)]

        self.theory[2][3] = 1

        self.setWindowTitle("Better FFCS")

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        # self.choose_slot_label()

        self.slots()


        # self.next_button()

        self.show()

    def slots(self):
        for j in range(11):
                temp = QLabel(f"Time{j}")
                temp.setAlignment(QtCore.Qt.AlignCenter)
                temp.setStyleSheet("border: 1px solid black;")

                self.grid.addWidget(temp, 0, j)


        for i in range(5):
            for j in range(5):
                temp = QPushButton(f"T{i}{j}\nTeacher{i}\nPRP208")

                if self.theory[i][j] == 1:
                    temp.setStyleSheet("background-color: cyan")
                else:
                    # temp.setAlignment(QtCore.Qt.AlignCenter)
                    temp.setStyleSheet("border: 1px solid black;")

                self.grid.addWidget(temp, i+1, j)

            temp = QLabel(f"Break")
            temp.setAlignment(QtCore.Qt.AlignCenter)
            temp.setStyleSheet("border: 1px solid black;")
            self.grid.addWidget(temp, i+1, 5)

        for i in range(5):
            for j in range(5):
                temp = QLabel(f"L{i}{j}\nTeacher{i}\nPRP208")
                temp.setAlignment(QtCore.Qt.AlignCenter)
                temp.setAlignment(QtCore.Qt.AlignCenter)
                temp.setStyleSheet("border: 1px solid black;")


                self.grid.addWidget(temp, i+1, 6+j)
            



    def next_button(self):
        next_button = QPushButton()

        self.layout().addWidget(next_button)


    def choose_slot_label(self):
        label = QLabel("Choose your preferred slot\n")

        # self.layout().addWidget(label)
        self.grid.addWidget(label)



app = QApplication(sys.argv)
subjects_window = DisplayTimetables()
sys.exit(app.exec_())
