# 4. Дан массив A размера N. Вывести его элементы в следующем порядке: A1, AN , A2, AN−1, A3, AN−2,


arr = [1, 2, 3, 4, 5, 6]

# Идем до середины массива
for i in range((len(arr) + 1) // 2):
    print(arr[i], end=" ") 
    if i != len(arr) - 1 - i: 
        print(arr[len(arr) - 1 - i], end=" ") 

print()