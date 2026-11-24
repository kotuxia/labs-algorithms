#4. Дано вещественное число A и целое число N (> 0). Используя один цикл, найти сумму 1 + A + A2 + A3 + . . . + AN

a = float(input("Введите вещественное число A: "))
n = int(input("Введите целое число N (> 0): "))

if n > 0:
    total_sum = 1.0
    current_term = 1.0
    i = 1
    
    while i <= n:
        current_term = current_term * a
        total_sum = total_sum + current_term
        i += 1
        
    print(f"\nИтоговая сумма: {total_sum}")
else:
    print("N должно быть больше 0")