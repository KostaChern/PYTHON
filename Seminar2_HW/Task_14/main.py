# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("введите целое число N, > 0  ==> "))

i = 1

while 2**i < n:
    print(2**i)
    i += 1


    

