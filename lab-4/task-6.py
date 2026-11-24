# 6. Обратный порядок слов: Напишите функцию, которая рекурсивно меняет порядок слов в заданной строке на обратный.

def reverse_words(s):
    if " " not in s:
        return s
    
    first_word, rest_of_string = s.split(" ", 1)
    
    return reverse_words(rest_of_string) + " " + first_word

text = input("Введите строку: ")
print(f"Результат: {reverse_words(text)}")