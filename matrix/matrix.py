class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.turn_matrix_string_into_matrix(matrix_string)

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        result = [el[index] for el in self.matrix]
        return result

    def turn_matrix_string_into_matrix(self, matrix_string):
        result = []
        matrix = matrix_string.split('\n')
        for row in matrix:
            new_row = row.split(' ')
            result.append([int(el) for el in new_row])
        return result