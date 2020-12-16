def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    valid_range = set()
    i = 0

    for line in lines:
        if line == "":
            i += 1
            break

        curr_line = line.split(": ")[1].split(" or ")
        range_1 = curr_line[0].split("-")
        range_2 = curr_line[1].split("-")

        range_1 = list(range(int(range_1[0]), int(range_1[1])+1))
        range_2 = list(range(int(range_2[0]), int(range_2[1]) + 1))

        valid_range.update(range_1)
        valid_range.update(range_2)

        i += 1

    my_ticket = [int(x) for x in lines[i+1].split(",")]

    while lines[i] != "":
        i += 1

    valid_tickets = []
    error_rate = 0
    print(lines[i+1])
    for j in range(i+2, len(lines)):
        is_valid = True

        numbers = [int(x) for x in lines[j].split(",")]

        for number in numbers:
            if number not in valid_range:
                is_valid = False
                error_rate += number
                break

        if is_valid:
            valid_tickets.append(numbers)

    return error_rate

print(problem1())
