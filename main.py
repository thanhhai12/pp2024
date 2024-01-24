from pw4.domains.student import Student
from pw4.domains.course import Course
from pw4.domains.mark import Mark
from pw4.input import input_students, input_courses, input_student_marks
from pw4.output import decorate_ui_with_curses

def main():
    mark_management_system = Mark()
    input_students(mark_management_system)
    input_courses(mark_management_system)
    input_student_marks(mark_management_system)

    mark_management_system.calculate_and_sort_by_gpa()
    decorate_ui_with_curses(mark_management_system)

if __name__ == "__main__":
    main()
