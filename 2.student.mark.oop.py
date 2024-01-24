class Student:
    def __init__(self, student_id, name, dob):
        self.student_id - student_id
        self.name = name
        self.dob = dob
        self.marks =
    def add_mark( se {}
        lf, course_id, marks):
        self.marks[course_id] = marks
    def get_marks(self, course_id):
        return self.marks.get(course_id, "N/A")
class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        
class Mark:
    def __init__(self):
        self.students = []
        self.courses = []
        
    def input_students(self):
        num_students = int(inpt("Enter the number of students:"))
        for _ in range(num_students):
            student_id = input("Enter the ID of student:")
            name = input("Enter the student's name:")
            dob = input("Enter the birtday of student: ")
            student = Students(student_id, name, dob)
            self.students.append(student)
            
    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.courses.append(course)
            
    def input_student_marks(self):
        student_id = input("Enter student ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            self.list_courses()
            course_id = input("Select a course (Enter course ID): ")
            marks = float(input(f"Enter marks for {student.name} in {course_id}: "))
            student.add_mark(course_id, marks)
        else:
            print("Student not found.")
            
    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"{course.course_id}"):{course.name}
    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"{student.student_id}: {student.name}")
    def show_student_marks(self):
        student_id = input("Enter student ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            self.list_courses()
            course_id = input("Select a course:")
            mark = student.get_marks(course_id)
            print("fMarks for {student.name} in {course_id}: {marks}")
        else:
            print("Student not found.")
            
def main():
    mark_management_system = Mark()
    mark_management_system.input_students()
    mark_management_system.input_courses()
    mark_management_system.input_student_marks()
    mark_management_system.list_students()
    mark_management_system.show_student_marks()

if __name__ == "__main__":
    main()