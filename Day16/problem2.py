def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    field_ranges = []
    i = 0

    for line in lines:
        if line == "":
            i += 1
            break

        curr_line = line.split(": ")[1].split(" or ")
        range_1 = curr_line[0].split("-")
        range_2 = curr_line[1].split("-")

        range_1 = list(range(int(range_1[0]), int(range_1[1]) + 1))
        range_2 = list(range(int(range_2[0]), int(range_2[1]) + 1))

        curr_range = range_1 + range_2
        field_ranges.append(curr_range)

        i += 1

    my_ticket = [int(x) for x in lines[i+1].split(",")]

    while lines[i] != "":
        i += 1

    valid_tickets = []

    for j in range(i+2, len(lines)):
        is_valid = True

        numbers = [int(x) for x in lines[j].split(",")]

        for number in numbers:
            if not any(number in sublist for sublist in field_ranges):
                is_valid = False
                break

        if is_valid:
            valid_tickets.append(numbers)

    fields_valid_positions = []

    for field_range in field_ranges:
        invalid_positions = set()

        for ticket in valid_tickets:
            for index, number in enumerate(ticket):
                if number not in field_range:
                    invalid_positions.add(index)

        valid_positions = set(list(range(len(my_ticket))))
        fields_valid_positions.append(valid_positions-invalid_positions)

    order = []
    filled = set()

    for i in range(len(my_ticket)):
        for index, field in enumerate(fields_valid_positions):
            if len(field) == i:
                new_field = field-filled
                order.append(index)
                filled.add(new_field.pop())

    print(order)

    answer = 1

    for i in range(6):
        for j in range(len(order)):
            if order[j] == i:
                answer *= my_ticket[j]
    print(answer)
    exit()

    return 0

print(problem1())

# 780167606843 too high
# 574755500971 too high