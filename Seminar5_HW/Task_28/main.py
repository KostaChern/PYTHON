# # Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

a = int(input("введте первое число ==>"))
b = int(input("введте второе число ==>"))

def summ_(a, b):
    if a == 0:
        return b
    else:
        return summ_(a - 1, b + 1)

print(summ_(a, b))