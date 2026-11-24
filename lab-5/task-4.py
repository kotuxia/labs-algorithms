# 4. Дан массив A размера N. Вывести его элементы в следующем порядке: A1, AN , A2, AN−1, A3, AN−2,


n = int(input("Введите размер массива N: "))
user_input = input(f"Введите {n} элементов через пробел: ")
arr = list(map(int, user_input.split()))

if len(arr) != n:
    print(f"вы ввели {len(arr)} элементов, а нужно {n}")
else:
    print("Элементы в нужном порядке:")
    
    for i in range((len(arr) + 1) // 2):
        print(arr[i], end=" ") 
        if i != len(arr) - 1 - i: 
            print(arr[len(arr) - 1 - i], end=" ") 

    print() 