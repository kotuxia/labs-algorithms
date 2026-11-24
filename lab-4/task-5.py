# 5. Бинарный поиск: Напишите функцию, которая рекурсивно выполняет бинарный поиск заданного элемента в отсортированном массиве.

def binary_search(arr, target, left, right):
    if left > right:  
        return -1
    
    mid = (left + right) // 2 
    
    if arr[mid] == target:     
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_num = int(input("Введите число для поиска: "))

result = binary_search(my_array, target_num, 0, len(my_array) - 1)
if result != -1:
    print(f"Число найдено на индексе {result}")
else:
    print("Число не найдено в массиве.")