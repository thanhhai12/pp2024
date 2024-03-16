from pw6.domains.student import Student
from pw6.domains.course import Course
from pw6.domains.mark import Mark
from pw6.input import input_students, input_courses, input_student_marks
from pw6.output import decorate_ui_with_curses

def main():
    # Check if students.dat exists
    try:
        mark_management_system = MarkManagementSystem()
        mark_management_system.students = load_data_from_file("students.dat")
    except FileNotFoundError:
        mark_management_system = MarkManagementSystem()
        
if __name__ == "__main__":
    main()