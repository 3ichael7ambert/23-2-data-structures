def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """


    size = len(matrix)
    sum = 0
    for i in range(size):
        sum += matrix[i][i]  # add element in TL-to-BR diagonal
        sum += matrix[i][size-i-1]  # add element in BL-to-TR diagonal
    return sum

m1 = [
        [1,   2],
        [30, 40],
    ]
m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
     ]

print("Should be 73: ",sum_up_diagonals(m1))
print("Should be 30: ",sum_up_diagonals(m2))