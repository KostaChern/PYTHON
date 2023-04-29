# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_array=[random.randint(-50, 50) for i in range(random.randint(10,20))]

print(*my_array)

max_i=int(input("Задайте MAX= "))

min_i=int(input("Задайте MIN= "))

my_arrayi=[]

if max_i>=min_i:

   for i in range(len(my_array)):

      if max_i>=my_array[i] and min_i<=my_array[i]:

          my_arrayi.append(i)

   print("Элементов в  заданном диапазоне :",len(my_arrayi))

   print("Индексы элементов:",my_arrayi)