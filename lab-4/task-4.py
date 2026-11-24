# 4. Палиндром: Напишите функцию, которая рекурсивно проверяет, является ли заданная строка палиндромом.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:  
        return True
    if s[0] != s[-1]: 
        return False
    
    return is_palindrome(s[1:-1])

word = input("Введите строку: ")
if is_palindrome(word):
    print("Это палиндром!")
else:
    print("Это не палиндром.")