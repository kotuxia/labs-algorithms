# 3. Дана матрица размера M × N. Найти номер ее столбца с наименьшим произведением элементов и
# вывести данный номер, а также значение наименьшего произведения.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

min_prod = float('inf') 
min_col_index = -1

for j in range(len(matrix[0])):
    current_prod = 1
    for i in range(len(matrix)):
        current_prod *= matrix[i][j] 
    
    if current_prod < min_prod:
        min_prod = current_prod
        min_col_index = j 

print(f"Номер столбца с наименьшим произведением (с 1): {min_col_index + 1}")
print(f"Наименьшее произведение: {min_prod}")