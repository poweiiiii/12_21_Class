import numpy as np
import sys
import json
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget, QTextBrowser, QMessageBox
from PyQt6.QtCore import Qt
from openpyxl import Workbook



class Student():
    def __init__(self , student_id ,name , connection):
        self.student_id = student_id
        self.name = name
        self.courses = {}
        self.connection = connection

    def Add_course(self , course_code , course_name , semester):
        if semester not in self.courses:
            self.courses[semester] = []
        [semester].append({"code": course_code, "name": course_name})

    def query_course_info(self , semester):
        if semester in self.courses:
            course_in_semester = self.courses[semester]
            return f'Course taken by {self.courses} in {semester}:',course_in_semester

        else:
            return f"No courses found for {self.name} in semester {semester}.", None

    def get_all_courses_info(self):
        all_courses_info = []
        for courses , semester in self.courses.items():
            for course in self.courses:
                all_courses_info.append({   
                    'Student ID':self.student_id,
                    'Name':self.name,
                    'Semester':semester,
                    'Course Code':course["code"],
                    'Course Name':course["name"]
                })
        return all_courses_info

    def svae_to_database(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (self.student_id, self.name))
 
        for semester, courses in self.courses.items():
            for course in courses:
                cursor.execute("INSERT INTO courses (student_id, semester, course_code, course_name) VALUES (?, ?, ?, ?)",
                               (self.student_id, semester, course["code"], course["name"]))
 
        self.connection.commit()
        

    