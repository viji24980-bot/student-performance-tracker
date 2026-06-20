class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        return {
            "Name": self.name,
            "Roll Number": self.roll_number,
            "Grades": self.grades,
            "Average": self.calculate_average()
        }
