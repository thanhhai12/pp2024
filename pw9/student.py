class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, marks):
        self.marks[course_id] = marks

    def get_marks(self, course_id):
        return self.marks.get(course_id, "N/A")

    def calculate_gpa(self):
        total_weighted_sum = 0
        total_credits = 0
        for course_id, marks in self.marks.items():
            total_weighted_sum += marks
            total_credits += 1

        if total_credits == 0:
            return 0

        gpa = round(sum(self.marks.values()) / total_credits, 1)
        return gpa
