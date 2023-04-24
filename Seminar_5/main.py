# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи









# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random
# marks=[random.randint(1,5) for _ in range(10)]
# print(marks)
# max_marks=max(marks)
# print(max_marks)
# min_marks=min(marks)
# for i in range (len(marks)):
#     if marks[i]==max_marks: marks[i]=min_marks
# print(marks)



# import random

# num=10
# array=[]

# for i in range(num):array.append(random.randint(1,5))
# print(array)

# max_point=max(array)
# min_point=min(array)

# for i in range(num):
#     if array[i]==max_point:
#         array[i]=min_point
# print(array)

# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")


#     a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")


# number=int(input( ))
# n=2
# while number%n!=0:
#      n+=1
# if n==number: print("простое число")
# else: print(" не простое число")



# def is_simple(num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         for i in range(3, num // 2, 2):
#             if num % i == 0:
#                 return False
#     return True


# num = int(input('Введите число: '))
# print(f'Число {num} ' + ('простое' if is_simple(num) else 'составное'))




# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).


def print_sequence(n: int, s='')-> str:
    if n != 0:
        s = s + str (n-1)
        return print_sequence(n - 1, s)
    else:
        return str(s)
n= int(input('Введите N: '))
print(print_sequence(n))