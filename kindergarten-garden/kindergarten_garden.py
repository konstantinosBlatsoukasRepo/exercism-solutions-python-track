DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                    'Ginny',  'Harriet', 'Ileana',  'Joseph',  'Kincaid', 'Larry']

PLANTS = {'C': 'Clover', 'G': 'Grass', 'V': 'Violets', 'R': 'Radishes'}

student_plants = {}


class Garden(object):

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        rows = diagram.splitlines()
        first_row = rows[0]
        second_row = rows[1]

        if students != DEFAULT_STUDENTS:
            students.sort()

        current_student_index = 0
        for index in range(0, len(first_row), 2):
            current_student = students[current_student_index]
            current_plants = self.__build_plants(first_row, second_row, index)
            student_plants[current_student] = current_plants
            current_student_index += 1

    def __build_plants(self, first_row, second_row, index):
        plants = []
        plants.append(PLANTS[first_row[index]])
        plants.append(PLANTS[first_row[index + 1]])
        plants.append(PLANTS[second_row[index]])
        plants.append(PLANTS[second_row[index + 1]])
        return plants

    def plants(self, student):
        return student_plants[student]
