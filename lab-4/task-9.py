# 9. Напишите рекурсивное решение головоломки "Ханойская башня".

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Диск 1: {source} -> {target}")
        return
    
    hanoi(n - 1, source, auxiliary, target)
    
    print(f"Диск {n}: {source} -> {target}")
    
    hanoi(n - 1, auxiliary, target, source)

n = int(input("Введите количество дисков: "))
if n > 0:
    print(f"Шаги для переноса {n} дисков:")
    hanoi(n, 'A', 'C', 'B')  
else:
    print("количество дисков должно быть больше 0")