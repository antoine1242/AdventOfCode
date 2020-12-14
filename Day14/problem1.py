def problem1():
    with open("input1.txt") as f:
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

            binary_number = (str(bin(int(number)))[2:].zfill(36))

            for index, bit in enumerate(curr_mask):
                if bit != "X":
                    binary_number = binary_number[:index] + bit + binary_number[index+1:]

            binary_number = int(binary_number, 2)
            memory[memory_spot] = binary_number

        i += 1

    sum = 0

    for key, value in memory.items():
        sum += value

    return sum


print(problem1())

# 9728560450906
# 9612920373496