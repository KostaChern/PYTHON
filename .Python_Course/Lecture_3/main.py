# Функции

# 1. сумма чисел

# def sum_nambers(n, y = "hellow"):
#     summa = 0
#     print(y)
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_nambers(5, "qwerty"))


# Передача неограниченного количества аргументов

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str("q", "w", "e", "r"))
# print(sum_str("q", "w", "e", "r", "t", "y"))
# # print(sum_str(1, 3, 6))



# Импорт функций

# from modul_1 import max_1
# import modul_1 as m1                # можно заменить название функции при вызове на более короткое


# print(m1.max_1(10, 9))



# РЕКУРСИЯ (функция, которая вызывает сама себя)

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 22):
#     list_1.append(fib(i))

# print(list_1)








# Быстрая сортировка


# def quick_sort(array):
#     if len(array)  <= 1:
#         return(array)
     
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 2 ]))


# МЕТОД слияния

def merge_sort(numbs):
    if len(numbs) > 1:
        mid = len(numbs) // 2
        left = numbs[:mid]
        right = numbs[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbs[k] = left[i]
                i += 1
            else:
                numbs[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbs[k] = right[j]
            j += 1
            k += 1

list_1 = [1,9,5,24,16,85,13,12,23,15,17,32,2]
merge_sort(list_1)
print(list_1)
            


    
