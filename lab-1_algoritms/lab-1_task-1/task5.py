a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))

if a == 0 or b == 0:
    print("Ошибка: числа должны быть ненулевыми")
else:
    a_abs = abs(a)
    b_abs = abs(b)

    summ = a_abs + b_abs
    diff = a_abs - b_abs
    prod = a_abs * b_abs
    quot = a_abs / b_abs

    print(f"Сумма модулей: {summ}")
    print(f"Разность модулей: {diff}")
    print(f"Произведение модулей: {prod}")
    print(f"Частное модулей: {quot}")