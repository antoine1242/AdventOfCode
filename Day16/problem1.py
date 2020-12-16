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

    for j in range(i+2, len(lines)):
        is_valid = True

        numbers = [int(x) for x in lines[j].split(",")]

        for number in numbers:
            if number not in valid_range:
                is_valid = False
                break

        if is_valid:
            valid_tickets.append(numbers)

    departure_fields_range = []

    departure_location_range = lines[0].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_location_range)
    departure_station_range = lines[1].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_station_range)
    departure_platform_range = lines[2].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_platform_range)
    departure_track_range = lines[3].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_track_range)
    departure_date_range = lines[4].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_date_range)
    departure_time_range = lines[5].split(": ")[1].split(" or ")
    departure_fields_range.append(departure_time_range)

    answer = 1

    for departure_range in departure_fields_range:
        departure_range_1 = departure_range[0].split("-")
        departure_range_1 = list(range(int(departure_range_1[0]), int(departure_range_1[1])+1))

        departure_range_2 = departure_range[1].split("-")
        departure_range_2 = list(range(int(departure_range_2[0]), int(departure_range_2[1]) + 1))

        combined_range = departure_range_1 + departure_range_2

        valid_position = sum(list(range(len(my_ticket))))
        invalid_positions = set()

        for ticket in valid_tickets:
            for index, value in enumerate(ticket):
                if value not in combined_range:
                    print(ticket)
                    print(value)
                    invalid_positions.add(index)
        print(combined_range)
        print(invalid_positions)
        print(valid_position)
        valid_position = valid_position - sum(invalid_positions)
        print(valid_position)
        exit()

    return 0

print(problem1())
