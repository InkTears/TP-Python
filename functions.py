if __name__ == '__main__':
    pass

def several_zeros():
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

def my_sort(my_list: [int]) -> [int]:
    sorted_list = my_list[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


class Matrix:
    def __init__(self, rows, cols):
        self._matrix = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        return self._matrix[row][col]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self._matrix == other._matrix





