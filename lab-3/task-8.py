# 8. Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых 
# сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму.

n = int(input("Введите целое число N (> 1): "))

if n > 1:
    k = 1
    total_sum = 0
    
    while total_sum < n:
        total_sum = total_sum + k
        k = k + 1 
        
    k = k - 1
    
    print(f"Наименьшее K: {k}")
    print(f"Сумма: {total_sum}")
else:
    print("N должно быть больше 1")