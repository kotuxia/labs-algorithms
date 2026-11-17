a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))

if a != b:
    if a > b:
        b = a
    else:
        a = b
else:
    a = 0
    b = 0

print(f"Новые значения: a = {a}, b = {b}")