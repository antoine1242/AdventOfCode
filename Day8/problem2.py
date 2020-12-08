def try_configuration(lines):
    index = 0
    accumulator = 0
    seen = set()

    while (True):
        if index in seen:
            return None

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

        if index == len(lines):
            return accumulator

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = [x.strip().split(" ") for x in content]

    for index in range(len(lines) - 1):
        if lines[index][0] == "jmp":
            lines[index][0] = "nop"
            ans = try_configuration(lines)
            if not ans == None:
                return ans
            else:
                lines[index][0] = "jmp"

        elif lines[index][0] == "nop":
            lines[index][0] = "jmp"
            ans = try_configuration(lines)
            if not ans == None:
                return ans
            else:
                lines[index][0] = "nop"


print(problem2())
