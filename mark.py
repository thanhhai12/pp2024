class Mark:
    def __init__(self):
        self.students = []
        self.courses = []

    def round_down_to_1_digit_decimal(self, value):
        return round(value * 10) / 10

    def calculate_and_sort_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)
