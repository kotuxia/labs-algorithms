# 7. Дан целочисленный массив размера N, не содержащий одинаковых чисел. Проверить, образуют
# ли его элементы арифметическую прогрессию. Если образуют, то вывести разность прогрессии, если нет — вывести 0.

arr = [5, 10, 15, 20] 

diff = arr[1] - arr[0]
is_progression = True

for i in range(1, len(arr) - 1):
    if arr[i+1] - arr[i] != diff:
        is_progression = False
        break

if is_progression:
    print(f"Это арифметическая прогрессия. Разность: {diff}")
else:
    print("0")