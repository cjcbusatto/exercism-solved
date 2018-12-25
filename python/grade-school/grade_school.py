class School(object):
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        return [name for name, grade in sorted(self.students.items(), key=lambda keyvalue: (keyvalue[1], keyvalue[0]))]

    def grade(self, grade_number):
        return sorted([student for student, grade in self.students.items() if grade == grade_number])
