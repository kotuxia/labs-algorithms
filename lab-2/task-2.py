# 2. Даны три числа. Найти сумму двух наибольших из них

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

sum_two_max = (a + b + c) - min_num

print(f"Сумма двух наибольших чисел: {sum_two_max}")