# 10. Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали,
# параллельной главной (начиная с одноэлементной диагонали).

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = len(matrix)

diagonals = {}

for i in range(m):
    for j in range(m):
        diff = j - i 
        if diff in diagonals:
            diagonals[diff] += matrix[i][j]
        else:
            diagonals[diff] = matrix[i][j]


for diff in sorted(diagonals.keys()):
    print(f"Диагональ (сдвиг {diff}): Сумма = {diagonals[diff]}")