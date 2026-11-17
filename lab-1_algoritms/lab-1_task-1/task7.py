A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))

ac = abs(A - C)
bc = abs(B - C)
summ = ac + bc

print(f"Длина отрезка AC: {ac}")
print(f"Длина отрезка BC: {bc}")
print(f"Сумма длин отрезков: {summ}")