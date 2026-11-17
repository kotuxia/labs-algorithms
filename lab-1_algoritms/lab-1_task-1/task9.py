x1 = float(input("Введите координату x1: "))
y1 = float(input("Введите координату y1: "))
x2 = float(input("Введите координату x2: "))
y2 = float(input("Введите координату y2: "))

width = abs(x2 - x1)
height = abs(y2 - y1)

s = width * height
p = 2 * (width + height)

print(f"Площадь прямоугольника: {s}")
print(f"Периметр прямоугольника: {p}")