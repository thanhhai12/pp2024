import gzip
import pickle
import json
import threading


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
    
    def save_data_to_file_async(filename, data):
        def save():
            with gzip.open(filename, 'wb') as file:
                pickle.dump(data, file)

        thread = threading.Thread(target=save)
        thread.start()

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


def input_students(mark_management_system):
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter the ID of student: ")
        name = input("Enter the student's name: ")
        dob = input("Enter the birthday of student: ")
        student = Student(student_id, name, dob)
        mark_management_system.students.append(student)

    # Write student info to students.txt
    with open("students.txt", "w") as file:
        for student in mark_management_system.students:
            file.write(f"{student.student_id},{student.name},{student.dob}\n")

    # Save data to compressed file students.dat in a background thread
    save_data_to_file_async("students.dat", mark_management_system.students)
    
def input_courses(mark_management_system):
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(course_id, name)
        mark_management_system.courses.append(course)

   # Write course info to courses.txt
    with open("courses.txt", "w") as file:
        for course in mark_management_system.courses:
            file.write(f"{course.course_id},{course.name}\n")

    # Save data to compressed file students.dat in a background thread
    save_data_to_file_async("students.dat", mark_management_system.students)
    
def input_student_marks(mark_management_system):
    student_id = input("Enter student ID: ")
    student = next((s for s in mark_management_system.students if s.student_id == student_id), None)
    if student:
        mark_management_system.list_courses()
        course_id = input("Select a course (Enter course ID): ")
        marks = float(input(f"Enter marks for {student.name} in {course_id}: "))
        marks = mark_management_system.round_down_to_1_digit_decimal(marks)
        student.add_mark(course_id, marks)

        # Write marks to marks.txt
    with open("marks.txt", "a") as file:
        file.write(f"{student_id},{course_id},{marks}\n")

     # Save data to compressed file students.dat in a background thread
    save_data_to_file_async("students.dat", mark_management_system.students)
    
    
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


# Example usage
input_students(mark_management_system)
input_courses(mark_management_system)
input_student_marks(mark_management_system)