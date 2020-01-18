import random
import math


def runnian(year):
    if not isinstance(year, int):
        print("year must be an integer")
    else:
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False


def delodd():
    # 生成一个包含50个整数的列表并删除其中所有奇数
    l = [random.randint(0, 100) for i in range(50)]
    print(l)
    for i in l[::-1]:
        if i % 2 != 0:
            l.remove(i)
    print(l)


def delodd2():
    l = [random.randint(0, 100) for i in range(50)]
    for i in range(len(l))[::-1]:
        if l[i]%2 == 1:
            del l[i]
    print(l)


def sort1():
    l = [random.randint(0, 100) for i in range(20)]
    print(l)
    l2 = sorted(l[::2], reverse=True)
    for i in range(0, len(l), 2):
        l[i] = l2[i // 2]
    print(l)


def sort2():
    l = [random.randint(0, 100) for i in range(20)]
    print(l)
    l[::2] = sorted(l[::2], reverse=True)
    print(l)


def factordivid(integer):
    if integer > 1000:
        return
    else:
        result = []
        i = 2
        while True:
            if integer == 1:
                break
            if integer % i == 0:
                result.append(i)
                integer //= i
            else:
                i += 1
        print(integer, '=', '*'.join(map(str, result)))


def sumodd1():
    print(sum(range(1, 100, 2)))


def sumodd2():
    print(sum([i for i in range(100) if i % 2 != 0]))


def printprime():
    from itertools import permutations
    digits = (1, 2, 3, 4)

    def isPrime(n):
        if n == 1:
            return True
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    for i in range(1, len(digits) + 1):
        for number in permutations(digits, i):
            number = int(''.join(map(str, number)))
            if isPrime(number):
                print(number)


def fenduanfunc(x):
    if x < 0 or x >= 20:
        print(0)
    elif x < 5:
        print(x)
    elif x >= 10:
        print(0.5 * x - 2)
    else:
        print(3 * x - 5)
