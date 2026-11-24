#2. Дано целое число N (> 0). Найти произведение 1.1 · 1.2 · 1.3 · . . . (N сомножителей).

n = int(input("Введите целое число N (> 0): "))

if n > 0:
    product = 1.0
    i = 1
    
    while i <= n:
        term = 1 + i * 0.1
        product = product * term
        i += 1
        
    print(f"Произведение {n} сомножителей: {product}")
else:
    print("N должно быть больше 0")