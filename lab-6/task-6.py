# 6. Дана матрица размера M × N. Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.

matrix = [
    [3, 1, 5],
    [9, 2, 4],
    [6, 8, 7]
]

for i in range(len(matrix)):
    min_idx = matrix[i].index(min(matrix[i]))
    max_idx = matrix[i].index(max(matrix[i]))
    
    # Меняем местами
    matrix[i][min_idx], matrix[i][max_idx] = matrix[i][max_idx], matrix[i][min_idx]

print("Матрица после замены:")
for row in matrix:
    print(row)