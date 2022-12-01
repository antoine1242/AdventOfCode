from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    buses = lines[1].split(",")
    numbers = []
    rests = []

    for i in range(len(buses)):
        if buses[i] != "x":
            numbers.append(int(buses[i]))
            rests.append(int(buses[i]) - i)

    return chinese_remainder(numbers, rests)

print(problem2())
