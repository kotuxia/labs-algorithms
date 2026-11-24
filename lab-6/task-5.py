# 5. Дана целочисленная матрица размера M × N. Найти номер первого из ее столбцов, содержащих 
# только нечетные числа. Если таких столбцов нет, то вывести 0.

matrix = [
    [2, 3, 1],
    [4, 5, 3],
    [6, 7, 5]
]

found_col = 0 
for j in range(len(matrix[0])):
    is_all_odd = True
    for i in range(len(matrix)):
        if matrix[i][j] % 2 == 0: 
            is_all_odd = False
            break
    
    if is_all_odd:
        found_col = j + 1
        break

print(f"Номер первого столбца из нечетных чисел (или 0): {found_col}")