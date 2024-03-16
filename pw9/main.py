from pw8.domains.student import Student
from pw8.domains.course import Course
from pw8.domains.mark import Mark
from pw8.input import input_students, input_courses, input_student_marks
from pw8.output import decorate_ui_with_curses

def main():
    mark_management_system = MarkManagementSystem()

    def on_closing():
        save_data_to_file_async("students.dat", mark_management_system.students)
        root.destroy()

    root = tk.Tk()
    root.title("Mark Management System")

    # Create and pack widgets for student input
    frame_students = ttk.Frame(root, padding="10")
    frame_students.grid(row=0, column=0, padx=10, pady=10)

    ttk.Label(frame_students, text="Student ID:").grid(row=0, column=0, sticky="W")
    entry_student_id = ttk.Entry(frame_students)
    entry_student_id.grid(row=0, column=1, pady=5)

    ttk.Label(frame_students, text="Name:").grid(row=1, column=0, sticky="W")
    entry_name = ttk.Entry(frame_students)
    entry_name.grid(row=1, column=1, pady=5)

    ttk.Label(frame_students, text="DOB:").grid(row=2, column=0, sticky="W")
    entry_dob = ttk.Entry(frame_students)
    entry_dob.grid(row=2, column=1, pady=5)

    btn_add_student = ttk.Button(frame_students, text="Add Student", command=lambda: input_students(mark_management_system, entry_student_id, entry_name, entry_dob))
    btn_add_student.grid(row=3, column=0, columnspan=2, pady=10)

    # Create and pack widgets for course input
    frame_courses = ttk.Frame(root, padding="10")
    frame_courses.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(frame_courses, text="Course ID:").grid(row=0, column=0, sticky="W")
    entry_course_id = ttk.Entry(frame_courses)
    entry_course_id.grid(row=0, column=1, pady=5)

    ttk.Label(frame_courses, text="Course Name:").grid(row=1, column=0, sticky="W")
    entry_course_name = ttk.Entry(frame_courses)
    entry_course_name.grid(row=1, column=1, pady=5)

    btn_add_course = ttk.Button(frame_courses, text="Add Course", command=lambda: input_courses(mark_management_system, entry_course_id, entry_course_name))
    btn_add_course.grid(row=2, column=0, columnspan=2, pady=10)

    # Create and pack widgets for inputting student marks
    frame_marks = ttk.Frame(root, padding="10")
    frame_marks.grid(row=0, column=2, padx=10, pady=10)

    ttk.Label(frame_marks, text="Student ID:").grid(row=0, column=0, sticky="W")
    entry_student_id_marks = ttk.Entry(frame_marks)
    entry_student_id_marks.grid(row=0, column=1, pady=5)

    ttk.Label(frame_marks, text="Course ID:").grid(row=1, column=0, sticky="W")
    entry_course_id_marks = ttk.Entry(frame_marks)
    entry_course_id_marks.grid(row=1, column=1, pady=5)

    ttk.Label(frame_marks, text="Marks:").grid(row=2, column=0, sticky="W")
    entry_marks = ttk.Entry(frame_marks)
    entry_marks.grid(row=2, column=1, pady=5)

    btn_add_marks = ttk.Button(frame_marks, text="Add Marks", command=lambda: input_student_marks(mark_management_system, entry_student_id_marks, entry_course_id_marks, entry_marks))
    btn_add_marks.grid(row=3, column=0, columnspan=2, pady=10)

    # Set up closing event
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
