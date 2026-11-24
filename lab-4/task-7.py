# 7. Разложение числа на сумму простых чисел: Напишите функцию, которая рекурсивно разлагает заданное число на сумму простых чисел.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def split_into_primes(n):
    if is_prime(n):
        return [n]
    
    for i in range(2, n):
        if is_prime(i):
            return [i] + split_into_primes(n - i)

n = int(input("Введите число для разложения: "))
if n > 1:
    result = split_into_primes(n)
    print(f"Разложение на простые числа: {' + '.join(map(str, result))}")
else:
    print("число должно быть больше 1")