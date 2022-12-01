def calculate_line(line):
    i = 0
    sum = 0
    curr_op = "+"
    curr_num = 0

    while i < len(line):
        if line[i].isdigit():
            curr_num = int(line[i])

            if curr_op == "+":
                sum += curr_num
            elif curr_op == "*":
                sum *= curr_num

        elif line[i] != "(":
            curr_op = line[i]

        else:
            curr_string = ""
            parenthesis = 1

            i += 1

            while parenthesis > 0:
                if line[i] == "(":
                    parenthesis += 1
                elif line[i] == ")":
                    parenthesis -= 1

                curr_string += line[i]

                i += 1

            curr_num = calculate_line(curr_string[:-1])

            if curr_op == "+":
                sum += curr_num
            elif curr_op == "*":
                sum *= curr_num

            i -= 1

        i += 1

    return sum

def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = ["".join(x.strip().split(" ")) for x in content]

    sum = 0

    for line in lines:
        sum += calculate_line(line)

    return sum

print(problem1())
