# 2. Числа Фибоначчи: Напишите функцию, которая рекурсивно вычисляет n-ое число Фибоначчи.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Введите номер числа Фибоначчи: "))
if n >= 0:
    print(f"Число Фибоначчи под номером {n} = {fibonacci(n)}")
else:
    print("Ошибка: номер должен быть >= 0")