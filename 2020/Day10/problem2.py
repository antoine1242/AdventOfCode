import copy
import itertools

def is_valid(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] not in [1, 2, 3]:
            return False

    return True

def compute_valids(length):
    valids = 0

    if length <= 2:
        return 1

    if length == 3:
        return 2

    numbers = list(range(1, length+1))

    for i in range(2, length+1):
        temp_numbers = numbers[1:-1]

        combinations = itertools.combinations(temp_numbers, length-i)

        for combination in combinations:
            if is_valid(numbers[0:1] + list(combination) + numbers[-1:]):
                valids += 1

    return valids

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    numbers = [int(x.strip()) for x in content]

    built_in = max(numbers) + 3

    numbers.append(0)
    numbers.append(built_in)

    numbers.sort()

    i = 0
    count_ones = 1
    valids = 1

    while i < len(numbers) - 1:
        if numbers[i+1] == numbers[i] + 1:
            count_ones += 1
        else:
            valids *= compute_valids(count_ones)
            count_ones = 1

        i += 1

    return valids

print(problem2())