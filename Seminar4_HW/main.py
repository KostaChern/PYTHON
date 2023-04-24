# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

array_nums_1 = int(input("Введите кол-во элементов первого множества: ==>  "))
import random
first_array = [random.randint(0, 50) for i in range(array_nums_1)]
print(first_array)
first_array = set(first_array)


array_nums_2 = int(input("Введите кол-во элементов второго множества: ==>  "))  
second_array = [random.randint(0, 50) for i in range(array_nums_2)]
print(second_array)
second_array = set(second_array)

itog_array = sorted(first_array.intersection(second_array))
print()
print(f"Числа, которые встречаются в обоих наборах ==> {itog_array}")
