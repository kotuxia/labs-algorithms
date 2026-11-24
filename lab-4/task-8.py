# 8. Подсчет количества цифр в числе: Напишите функцию, которая рекурсивно подсчитывает количество цифр в заданном числе.

def count_digits(n):
    if n < 10:  
        return 1
    else:
        return 1 + count_digits(n // 10)

num = int(input("Введите число: "))

print(f"Количество цифр: {count_digits(abs(num))}")