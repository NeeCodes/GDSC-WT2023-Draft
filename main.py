from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QLabel
import sys

from choose_slot_window import ChooseSlotWindow
from choose_subjects_window import ChooseSubjectsWindow
from display_time_table import DisplayTimetables
from subject_priority_window import SubjectPriorityWindow
from teacher_priority_window import TeacherPriorityWindow







app = QApplication(sys.argv)

choose_slot_window = ChooseSlotWindow()
# choose_subjects_window = ChooseSubjectsWindow()
# display_time_table = DisplayTimetables()
# subject_priority_window = SubjectPriorityWindow()
# teacher_priority_window = TeacherPriorityWindow()



sys.exit(app.exec_())