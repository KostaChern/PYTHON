#     СЕМИНАР 3: 
#  ЗАДАЧА: сдвинуть список вправо на А элементов

# list_1 = [i for i in range(1, 11)]
# print(list_1)

# shift = int(input('на сколько двигаем список вправо?'))
# for _ in range(shift):
#     list_1.insert(0, list_1.pop())

# # a = 3
# # b = (len(list_1))
# # new_list_1 = list_1[-a:] + list_1[:-a]

# print(list_1)

#  ЗАДАЧА: написать программу для печати всех уникальных значений в словаре

# list_1 = [{"Y": "1001"}, {'T': '8000'}, {"R": '4561'}]
# print(list_1)

# unicum_value = set()
# for element in list_1:
#     for value in element.values():
#         unicum_value.add(value)
# print(unicum_value)        

# res = set()
# for i in list_1:
#     for(k, v) in i.items():
#         res.add(v)
# print(res)


# ЗАДАЧА: 
# в списке из целых чисел, написать программу, подсчитывающую количество элементов списка, больше предыдущего
# 

# integer_list = [1, 2, 1, 4, 2, 6, 7, 1, 0, 9]

# count = 0
# for i in range(1, len(integer_list)):
#     if integer_list[i] > integer_list[i - 1]:
#         count += 1
# print(count)

