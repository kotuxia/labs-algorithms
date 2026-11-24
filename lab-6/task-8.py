# 8. Дана матрица размера M × N (M и N — четные числа). Поменять местами левую верхнюю и правую нижнюю четверти матрицы

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

m = len(matrix)
n = len(matrix[0])
half_m = m // 2
half_n = n // 2

for i in range(half_m):
    for j in range(half_n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i + half_m][j + half_n]
        matrix[i + half_m][j + half_n] = temp

print("Матрица после смены четвертей:")
for row in matrix:
    print(row)