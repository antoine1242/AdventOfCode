import regex

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = ["".join(x.strip().split(" ")) for x in content]

    sum = 0

    for line in lines:

        asterisk_exprs = regex.findall(r"\d\+\d", line)
        for expr in asterisk_exprs:
            line = line.replace(expr, "({})".format(expr))

        print(line)

        for i in range(len(line)):
            if line[i] == "+":
                if line[i-1].isdigit():
                    line = line[:i-1] + "(" + line[i-1:]
                    i += 1
                else:
                    j = i-1
                    count_parenthesis = 1
                    while j >=0 :
                        if line[j] == "(":
                            count_parenthesis -= 1
                        elif line[j] == ")":
                            count_parenthesis += 1

                        if count_parenthesis == 0:
                            line = line[:j-1] + "(" + line[j:]
                            i += 1
                            break
                        j -= 1

                if line[i+1].isdigit():
                    line = line[:i+2] + ")" + line[i+2:]
                    i += 1
                else:
                    j = i+1
                    count_parenthesis = 1
                    while j < len(line) :
                        if line[j] == ")":
                            count_parenthesis -= 1
                        elif line[j] == "(":
                            count_parenthesis += 1

                        if count_parenthesis == 0:
                            line = line[:j+1] + ")" + line[j+1:]
                            break
                        j += 1


        print(line)
        print(eval(line))
        sum += eval(line)

    return sum

print(problem2())

# 8603920057901 Too low
# 8603978269981 Too low