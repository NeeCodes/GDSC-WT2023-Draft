from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel
import sys

chosen_subjects = ["Differential Equations and Transforms",
            "Structured and Object Oriented Programming",
            "Technical English Communication",
            "Engineering Physics",
            "Data Structure and Algorithms",
            "Quantitative Skills I"]

class TeacherPriorityWindow(QtWidgets.QWidget):
    priority_list = [0 for i in range(len(chosen_subjects))]

    subjects = chosen_subjects

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Better FFCS")

        self.form_layout = QtWidgets.QFormLayout()
        self.setLayout(self.form_layout)

        self.subject_priority_label()


        self.combo_boxes()


        self.next_button()

        # self.show_subjects()

        self.show()

    def combo_boxes(self):
        # subjects = chosen_subjects

        self.combo_boxes = []
        self.priority_options = []

        # create the combo boxes but theyre disabled by default
        for i in range(len(chosen_subjects)):
            temp = QComboBox()
            self.combo_boxes.append(temp)
            # self.combo_boxes[i].setEnabled(False)

            # for subject in chosen_subjects:
            #     temp_subjects = chosen_subjects
            #     temp_subjects.remove(subject)

            #     self.combo_boxes[i].addItem(subject, temp_subjects)
            # self.combo_boxes[i].addItems(subjects)

            self.combo_boxes[i].addItems(self.subjects)

            self.form_layout.addRow(f"{i+1}", self.combo_boxes[i])

        # for combo_box in self.combo_boxes:
        #     combo_box.activated.connect(self.subject)
       

    def next_button_clicked(self):
        for i in range(len(self.combo_boxes)):
            subject = str(self.combo_boxes[i].currentText())

            self.priority_list[i] = subject

        print(self.priority_list)


    def next_button(self):
        next_button = QPushButton()
        next_button.clicked.connect(self.next_button_clicked)

        self.layout().addWidget(next_button)


    def subject_priority_label(self):
        label = QLabel("Choose your subject priority order\n")

        self.layout().addWidget(label)
     





app = QApplication(sys.argv)
subjects_window = TeacherPriorityWindow()
sys.exit(app.exec_())
