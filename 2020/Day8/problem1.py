def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip().split(" ") for x in content]

    index = 0
    accumulator = 0
    seen = set()

    while(True):
        if index in seen:
            return accumulator

        seen.add(index)

        operation = lines[index][0]
        argument = int(lines[index][1])

        if operation == "acc":
            accumulator += argument
            index += 1
        elif operation == "jmp":
            index += argument
        else:
            index += 1


    return 0

print(problem1())
