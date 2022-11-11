import random

def range_generation(v, w, x, y):
    array = [random.randint(x, y) for _ in range(random.randint(v, w))]
    return array

def common_divisor(num, den):   # сделаем свой math.gcd с преферансом и барышнями
    if num > den:
        divisor = num
    else:
        divisor = den
    while divisor != 1:
        if num % divisor == 0 and den % divisor == 0:
            return divisor
        else:
            divisor -= 1
    return divisor


# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def task01():

    n = random.randint(1, 1000)
    print(n)
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    print(f'{n} + {nn} + {nnn} = {n + nn + nnn}')

# task01()


# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def task02():

    nums = range_generation(10, 20, 1, 10)
    n = str(random.randint(100, 999))
    # nums = [0, 5, 6, 2, 7, 7, 8, 1, 1, 9, 4, 4, 3, 6, 7, 0, 8, 5, 1, 2]
    # n = input('Enter 3 digit num: ')
    print(n, nums, sep='\n')
    flag = 0
    for i in range(0, len(nums) - 2):
        if int(n[0]) == nums[i] and int(n[1]) == nums[i + 1] and int(n[2]) == nums[i + 2]:
            flag += 1
    print('Yes' if flag > 0 else 'No')

# task02()


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def task03():

    print('All simple irreducible fractions between 0 and 1 whose denominator doesn\'t exceed 11: ')
    for denominator in range(2, 12):
        for numerator in range(1, 12):
            if (numerator % denominator != 0) and (numerator / denominator < 1):    # можно через math.gcd
                if (common_divisor(numerator, denominator) != 2 and common_divisor(numerator, denominator) != 3 and     
                    common_divisor(numerator, denominator) != 4 and common_divisor(numerator, denominator) != 5):
                    print(f'{numerator}/{denominator}', end=' ')
        print()

task03()
