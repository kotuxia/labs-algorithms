# 4. Дана матрица размера M × N. В каждом ее столбце найти количество элементов, больших
# среднего арифметического всех элементов этого столбца

matrix = [
    [1, 5, 9],
    [2, 6, 1],
    [3, 7, 2]
]

for j in range(len(matrix[0])):
    # 1. сумму столбца
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    
    # 2. Среднее арифметическое
    avg = col_sum / len(matrix)
    
    # 3. сколько элементов больше среднего
    count = 0
    for i in range(len(matrix)):
        if matrix[i][j] > avg:
            count += 1
            
    print(f"В столбце {j+1} элементов больше среднего ({avg:.2f}): {count}")