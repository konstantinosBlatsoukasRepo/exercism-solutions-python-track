class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.matrix = self.__build_matrix(rows)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column_index = index - 1
        total_rows = len(self.matrix)

        column = []
        for current_row in range(0, total_rows):
            column.append(self.matrix[current_row][column_index])
        return column

    def __build_matrix(self, rows):
        matrix = []
        for row in rows:
            row_elements = row.split()
            current_row = self.__build_row(row_elements)
            matrix.append(current_row)
        return matrix

    def __build_row(self, row_elements):
        current_row = []
        for row_element in row_elements:
            current_row.append(int(row_element))
        return current_row
