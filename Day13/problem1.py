def problem1():
    with open("input1.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    buses_initial = lines[1].split(",")
    buses = []
    for bus in buses_initial:
        if bus != "x":
            buses.append(int(bus))

    initial_time = time = int(lines[0])

    found = False

    while not found:
        time += 1

        for bus in buses:
            if time % bus == 0:
                found = True
                bus_id = bus
                break

    return (time - initial_time) * bus_id

print(problem1())
