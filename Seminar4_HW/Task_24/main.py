# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по 
# окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки.


import random
bush = int(input("введите общее количество кустов: "))
berryes = list(random.randint(0, 30) for i in range(bush))
print(f"ягод на кустах по кругу ==> {berryes}")

berryes_count = list()
for i in range(len(berryes)-1):
    berryes_count.append(berryes[i] + berryes[i - 1] + berryes[i + 1])
berryes_count.append(berryes[0] + berryes[-1] + berryes[-2])

print(f"Наибольшее количество ягод за один подход ==> {max(berryes_count)}")

