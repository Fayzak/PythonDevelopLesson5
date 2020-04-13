import math


def num_div_max(n):
    max_div = 1
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            if max_div < i:
                max_div = i
    print(max_div)


def num_divs_canon(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    canon_divs = []
    for i in divs:
        canon_divs.append(i)
        canon_divs.append('^')
        canon_divs.append(divs.count(i))
    print(canon_divs)


def num_div_max_simple(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    max = 0
    for i in divs:
        temp = 0
        if temp < i:
            temp = i
            max = temp
    print(max)


def num_divs(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    print(divs)


def num_simple(n):
    if n < 2:
        print('Число не составное и не простое')
    elif n == 2:
        print('Простое число')
    else:
        i = 2
        lim = int(math.sqrt(n))
        while i <= lim:
            if n % i == 0:
                print('Составное число')
                quit()
            i += 1
        print('Простое число')



