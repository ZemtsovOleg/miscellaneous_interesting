import random

lst = [random.randint(0, 10) for _ in range(10)]


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]  # Выбираем опорный элемент
    
    lesser = [x for x in lst[1:] if x <= pivot]  # Подсписок элементов меньших или равных опорному
    greater = [x for x in lst[1:] if x > pivot]  # Подсписок элементов больших опорного
    
    return quicksort(lesser) + [pivot] + quicksort(greater)  # Рекурсивно сортируем и объединяем подсписки


def quick_sort(s):
    if len(s) < 2:
        return s
    x = s[0]
    return quick_sort([i for i in s[1:] if i < x]) + [i for i in s if i == x] + quick_sort([i for i in s[1:] if i > x])

print(quick_sort(lst))