def helper(index, lines):
    temp_lines = lines[index - 25: index ]

    for j in range(len(temp_lines)):
        for k in range(j, len(temp_lines)):
            if temp_lines[j] + temp_lines[k] == lines[index]:
                return True

    return False

def find_num(lines):
    for i in range(25, len(lines)):
        if helper(i, lines):
            continue
        else:
            return lines[i]

    return 0


def problem2():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [int(x.strip()) for x in content]

    number = find_num(lines)

    acc = 0

    for i in range(len(lines)):
        index = i
        acc += lines[index]

        while acc < number:
            index += 1
            acc += lines[index]

        if acc == number:
            return min(lines[i:index]) + max(lines[i:index])

        acc = 0

    return -1

print(problem2())
