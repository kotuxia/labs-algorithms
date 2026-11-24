# 7. Дана матрица размера M × N. Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы

matrix = [
    [3, 1, 5],
    [9, 2, 4],
    [6, 8, 7]
]

min_val = float('inf')
max_val = float('-inf')
min_col = 0
max_col = 0

# min и max и запоминаем ИХ СТОЛБЦЫ
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_col = j
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_col = j

# Меняем столбцы
for i in range(len(matrix)):
    matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

print("Матрица после замены столбцов:")
for row in matrix:
    print(row)