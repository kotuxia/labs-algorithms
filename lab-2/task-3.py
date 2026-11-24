# 3. На плоскости расположены три точки: A, B, C. Определить, какая из двух последних точек
# (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A.

import math

x1 = float(input("Введите координату A(x1): "))
y1 = float(input("Введите координату A(y1): "))
x2 = float(input("Введите координату B(x2): "))
y2 = float(input("Введите координату B(y2): "))
x3 = float(input("Введите координату C(x3): "))
y3 = float(input("Введите координату C(y3): "))

s_from_b_to_a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
s_from_c_to_a = math.sqrt((x3-x1)**2 + (y3-y1)**2)

if s_from_b_to_a < s_from_c_to_a:
    print(f"Ближайшая точка к A: B. Расстояние между ними: {s_from_b_to_a}")
elif s_from_b_to_a == s_from_c_to_a:
    print(f"Точки B и C равноудалены от A. Расстояние от них до A: {s_from_b_to_a}")
else: 
    print(f"Ближайшая точка к A: C. Расстояние между ними: {s_from_c_to_a}")