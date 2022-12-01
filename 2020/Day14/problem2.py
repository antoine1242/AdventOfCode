def get_floating_values(memory_spot):
    if "X" not in memory_spot:
        return [memory_spot]

    new_values_0 = []
    new_values_1 = []

    for index, bit in enumerate(memory_spot):
        if bit == "X":
            new_values_0 = get_floating_values(memory_spot[:index] + "0" + memory_spot[index + 1:])
            new_values_1 = get_floating_values(memory_spot[:index] + "1" + memory_spot[index + 1:])
            break

    return new_values_0 + new_values_1

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    i = 0
    curr_mask = ""
    memory = {}

    while True:
        if i == len(lines):
            break

        if lines[i].startswith("mask"):
            curr_mask = lines[i].split(" ")[2]

        else:
            memory_spot = lines[i].split(" ")[0]
            memory_spot = memory_spot[4:-1]

            number = lines[i].split(" ")[2]

            memory_spot = (str(bin(int(memory_spot)))[2:].zfill(36))

            for index, bit in enumerate(curr_mask):
                if bit != "0":
                    memory_spot = memory_spot[:index] + bit + memory_spot[index+1:]

            floating_values = get_floating_values(memory_spot)

            for spot in floating_values:
                memory[spot] = number

        i += 1

    sum = 0

    for key, value in memory.items():
        sum += int(value)

    return sum

print(problem2())
