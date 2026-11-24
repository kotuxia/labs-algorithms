# 5. Дано вещественное число A и целое число N (> 0). Используя один цикл, найти значение выражения 
# 1 − A + A2 − A3 + . . . ± AN . 
# Условный оператор не использовать.

a = float(input("Введите вещественное число A: "))
n = int(input("Введите целое число N (> 0): "))

if n > 0:
    total_sum = 1.0   
    current_term = 1.0
    sign = -1
    
    for i in range(1, n + 1):
        current_term = current_term * a  
        total_sum = total_sum + (current_term * sign) 
        sign = sign * -1  
        
    print(f"Значение выражения: {total_sum}")
else:
    print("N должно быть больше 0")