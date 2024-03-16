def input_students(mark_management_system):
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter the ID of student: ")
        name = input("Enter the student's name: ")
        dob = input("Enter the birthday of student: ")
        student = mark_management_system.Student(student_id, name, dob)
        mark_management_system.students.append(student)

def input_courses(mark_management_system):
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = mark_management_system.Course(course_id, name)
        mark_management_system.courses.append(course)

def input_student_marks(mark_management_system):
    student_id = input("Enter student ID: ")
    student = next((s for s in mark_management_system.students if s.student_id == student_id), None)
    if student:
        mark_management_system.list_courses()
        course_id = input("Select a course (Enter course ID): ")
        marks = float(input(f"Enter marks for {student.name} in {course_id}: "))
        marks = mark_management_system.round_down_to_1_digit_decimal(marks)
        student.add_mark(course_id, marks)
    else:
        print("Student not found.")
