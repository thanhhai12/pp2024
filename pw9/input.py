import gzip
import pickle
import json
import threading
import tkinter as tk
from tkinter import ttk

class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def list_courses(self):
        print("Available Courses:")
        for course in self.courses:
            print(f"{course.course_id}: {course.name}")

    def round_down_to_1_digit_decimal(self, number):
        return round(number, 1)

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

def save_data_to_file_async(filename, data):
    def save():
        with gzip.open(filename, 'wb') as file:
            pickle.dump(data, file)

    thread = threading.Thread(target=save)
    thread.start()

def load_data_from_file(filename):
    try:
        with gzip.open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def input_students(mark_management_system, entry_id, entry_name, entry_dob):
    student_id = entry_id.get()
    name = entry_name.get()
    dob = entry_dob.get()

    student = Student(student_id, name, dob)
    mark_management_system.students.append(student)

    save_data_to_file_async("students.dat", mark_management_system.students)

def input_courses(mark_management_system, entry_course_id, entry_course_name):
    course_id = entry_course_id.get()
    name = entry_course_name.get()

    course = Course(course_id, name)
    mark_management_system.courses.append(course)

    save_data_to_file_async("students.dat", mark_management_system.students)

def input_student_marks(mark_management_system, entry_student_id, entry_course_id, entry_marks):
    student_id = entry_student_id.get()
    student = next((s for s in mark_management_system.students if s.student_id == student_id), None)

    if student:
        mark_management_system.list_courses()
        course_id = entry_course_id.get()
        marks = float(entry_marks.get())
        marks = mark_management_system.round_down_to_1_digit_decimal(marks)
        student.add_mark(course_id, marks)

        save_data_to_file_async("students.dat", mark_management_system.students)
    else:
        print("Student not found.")


def compress_files(self):
        compression_method = input("Select compression method (pickle/bz2): ")
        if compression_method == "pickle":
            with open("students.dat", "wb") as file:
                pickle.dump((self.students, self.courses), file)
        elif compression_method == "bz2":
            with open("students.dat", "wb") as file:
                pickled_data = pickle.dumps((self.students, self.courses))
                compressed_data = bz2.compress(pickled_data)
                file.write(compressed_data)
        else:
            print("Invalid compression method.")

def decompress_files(self):
        try:
            with open("students.dat", "rb") as file:
                if file.read(2) == b'\x42\x5a':  # Magic number for bz2 files
                    file.seek(0)
                    compressed_data = file.read()
                    pickled_data = bz2.decompress(compressed_data)
                    self.students, self.courses = pickle.loads(pickled_data)
                else:
                    file.seek(0)
                    self.students, self.courses = pickle.load(file)
        except FileNotFoundError:
            print("File not found.")