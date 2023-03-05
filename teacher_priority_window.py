# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:00:20 2023

@author: WELCOME
"""

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel
import sys

chosen_subjects = ["Differential Equations and Transforms",
            "Structured and Object Oriented Programming",
            "Technical English Communication",
            "Engineering Physics",
            "Data Structure and Algorithms",
            "Quantitative Skills I"]
teachers=["t1","t2","t3","t4","t5"]
class SubjectPriorityWindow(QtWidgets.QWidget):
    priority_list = [0 for i in range(len(teachers))]
    l_teachers = teachers

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Better FFCS")
        self.setGeometry(100, 100, 540, 540)
        self.form_layout = QtWidgets.QFormLayout()
        self.setLayout(self.form_layout)
        self.label1 = QLabel(self)
        self.label1.resize(540, 540)
        self.label1.setStyleSheet("background-image:url(C:/Users/WELCOME/Downloads/WhatsApp Image 2023-03-05 at 08.26.53 (1).jpeg);border: 1px blue")
        # self.grid = QtWidgets.QGridLayout()
        # self.setLayout(self.grid)

        # self.setFixedSize(800, 600)

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
        for i in range(len(teachers)):
            label=self.label=QLabel(chosen_subjects[i])
            self.layout().addWidget(label)
            label.setStyleSheet("background-color:rgba(255,255,255,10)")
            temp = QComboBox()
            temp.setStyleSheet("background-color:rgba(255,255,255,10)")
            self.combo_boxes.append(temp)
            
            self.combo_boxes[i].addItems(self.l_teachers)
            
            self.form_layout.addRow(f"{i+1}", self.combo_boxes[i])
       

    def next_button_clicked(self):
        for i in range(len(self.combo_boxes)):
            subject = str(self.combo_boxes[i].currentText())
            
            self.priority_list[i] = subject

        print(self.priority_list)


    def next_button(self):
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_button_clicked)
        next_button.setStyleSheet("background-color:rgba(255,255,255,10)")
        self.layout().addWidget(next_button)


    def subject_priority_label(self):
        label = QLabel("Choose your teacher priority order\n")
        label.setStyleSheet("background-color:rgba(255,255,255,10)")
        self.layout().addWidget(label)     





app = QApplication(sys.argv)
subjects_window = SubjectPriorityWindow()
sys.exit(app.exec_())
