students = []

def add_student():
    student_id = input("Enter the ID of student: ")
    name = input("Enter the student's name: ")
    dob = input("Enter the birthday of student: ")
    student = {"id": student_id, "name": name, "dob": dob, "marks": {}}
    students.append(student)

def add_student_marks():
    student_id = input("Enter student ID: ")
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        course_id = input("Enter course ID: ")
        marks = float(input(f"Enter marks for {student['name']} in {course_id}: "))
        student["marks"][course_id] = marks
    else:
        print("Student not found.")

def list_students():
    print("\nList of Students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_student_marks():
    student_id = input("Enter student ID: ")
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        for course_id, marks in student["marks"].items():
            print(f"Marks for {student['name']} in {course_id}: {marks}")
    else:
        print("Student not found.")

def main():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        add_student()

    add_student_marks()
    list_students()
    show_student_marks()

if __name__ == "__main__":
    main()
