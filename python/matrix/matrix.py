class Matrix(object):
    def __init__(self, matrix_string):
        self.values = self._decode(matrix_string)

    def _decode(self, matrix_string):
        decoded_rows = matrix_string.split("\n")
        return [list(map(int, row.split())) for row in decoded_rows]

    def row(self, index):
        return self.values[index]

    def column(self, index):
        return [row[index] for row in self.values]
