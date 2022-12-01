import copy

def move_ship(curr_waypoint, curr_x, curr_y, command, number):
    if command == "E":
        curr_waypoint = (curr_waypoint[0] + number, curr_waypoint[1])
    elif command == "N":
        curr_waypoint = (curr_waypoint[0], curr_waypoint[1] + number)
    elif command == "S":
        curr_waypoint = (curr_waypoint[0], curr_waypoint[1] - number)
    elif command == "W":
        curr_waypoint = (curr_waypoint[0] - number, curr_waypoint[1])

    elif command == "R":
        turns = number // 90

        for i in range(turns):
            curr_waypoint = (curr_waypoint[1], -curr_waypoint[0])

    elif command == "L":
        turns = number // 90

        for i in range(turns):
            curr_waypoint = (-curr_waypoint[1], curr_waypoint[0])


    elif command == "F":
        curr_x += curr_waypoint[0] * number
        curr_y += curr_waypoint[1] * number

    return curr_waypoint, curr_x, curr_y

def problem2():
    with open("input2.txt") as f:
        content = f.readlines()
    lines = [x.strip() for x in content]

    curr_waypoint = (10, 1)
    curr_x = 0
    curr_y = 0

    for line in lines:
        command = line[0]
        number = int(line[1:])

        curr_waypoint, curr_x, curr_y = move_ship(curr_waypoint, curr_x, curr_y, command, number)

    return abs(curr_x) + abs(curr_y)
    
print(problem2())
