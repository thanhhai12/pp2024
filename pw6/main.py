from pw5.domains.student import Student
from pw5.domains.course import Course
from pw5.domains.mark import Mark
from pw5.input import input_students, input_courses, input_student_marks
from pw5.output import decorate_ui_with_curses

def main():
    # Check if students.dat exists
    try:
        mark_management_system = MarkManagementSystem()
        mark_management_system.students = load_data_from_file("students.dat")
    except FileNotFoundError:
        mark_management_system = MarkManagementSystem()
        
if __name__ == "__main__":
    main()