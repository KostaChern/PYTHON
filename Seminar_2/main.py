number = int(input("введите число >1 ==>"))

first = 0
second = 1

index = 1

while second < number:
    first, second = second, first + second
    index += 1

print(index if second == number else -1 )


    



 