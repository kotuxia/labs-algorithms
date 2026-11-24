# 3. Возведение в степень: Напишите функцию, которая рекурсивно возводит число x в степень n.

def power(x, n):
    if n == 0:  
        return 1
    else:     
        return x * power(x, n - 1)

x = float(input("Введите число x: "))
n = int(input("Введите степень n: "))

if n >= 0:
    print(f"{x} в степени {n} = {power(x, n)}")
else:
    print(f"{x} в степени {n} = {1 / power(x, -n)}")