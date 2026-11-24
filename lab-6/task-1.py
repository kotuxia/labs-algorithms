# 1. Дана квадратная матрица A порядка M (M — нечетное число). Начиная с элемента A1,1 и перемещаясь 
# против часовой стрелки, вывести все ее элементы по спирали: первый столбец, последняя строка, последний столбец в обратном порядке, первая строка в обратном порядке, оставшиеся элементы второго столбца и т. д.; 
# последним выводится центральный элемент матрицы.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = len(matrix)
n = len(matrix[0])

# Задаем границы
top = 0
bottom = m - 1
left = 0
right = n - 1

result = []

while top <= bottom and left <= right:
    for i in range(top, bottom + 1):
        result.append(matrix[i][left])
    left += 1 
    
    for j in range(left, right + 1):
        result.append(matrix[bottom][j])
    bottom -= 1 
    
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][right])
        right -= 1
        
    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[top][j])
        top += 1

print("Элементы по спирали:", result)