def problem2():
    with open("input2.txt") as f:
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
        if field_range[0] == 30:
            print("")
        invalid_positions = set()

        for ticket in valid_tickets:
            for index, number in enumerate(ticket):
                if number not in field_range:
                    invalid_positions.add(index)

        valid_positions = set(list(range(len(my_ticket))))
        fields_valid_positions.append(valid_positions-invalid_positions)

    order = list(range(len(my_ticket)))
    filled = set()

    for field in fields_valid_positions:
        print(field)

    for i in range(1, len(my_ticket) + 1):
        for index, field in enumerate(fields_valid_positions):
            if len(field) == i:
                new_field = field-filled
                new_field2 = field-filled
                order[index] = new_field.pop()
                filled.add(new_field2.pop())
                break

    answer = 1

    for i in range(6):
        answer *= my_ticket[order[i]]

    return answer

print(problem2())

# 366871907221
