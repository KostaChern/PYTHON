# Найти дружественные числа Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.


def divisors_sum(number):
    return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)


max_number = 10000
pairs = {}
for i in range(1, max_number + 1):
    aggr = divisors_sum(i)
    if i == divisors_sum(aggr) and i != aggr:
        if i and aggr not in pairs:
            pairs[i] = aggr
print(pairs)

