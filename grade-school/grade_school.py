from operator import itemgetter


class School(object):
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append((name, grade))
        self.students = sorted(self.students, key=itemgetter(1, 0))

    def roster(self):
        return [name for name, grade in self.students]

    def grade(self, grade_number):
        return [name for name, grade in self.students if grade_number == grade]
