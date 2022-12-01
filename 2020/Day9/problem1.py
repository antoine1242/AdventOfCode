def helper(index, lines):
    temp_lines = lines[index - 25: index ]

    for j in range(len(temp_lines)):
        for k in range(j, len(temp_lines)):
            if temp_lines[j] + temp_lines[k] == lines[index]:
                return True

    return False

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [int(x.strip()) for x in content]


    for i in range(25, len(lines)):
        if helper(i, lines):
            continue
        else:
            return lines[i]

    return 0

print(problem1())
