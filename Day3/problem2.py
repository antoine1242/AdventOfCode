import math

def run():
    with open("input.txt") as f:
        wire1 = f.readline()
        wire2 = f.readline()
    instructions1 = wire1.split(",")
    instructions2 = wire2.split(",")

    segments1 = get_segments_wire1(instructions1)

    min_distance = get_closest_intersection(instructions2, segments1, instructions1)

    print(min_distance)
    
def get_closest_intersection(instructions2, segments1, instructions1):
    currX = 0
    currY = 0 

    min_distance = math.inf

    for index2, instruction in enumerate(instructions2):
        point1 = (currX, currY)

        direction, num = read_instuction(instruction)

        if direction == "D":
            currY -= num

        elif direction == "U":
            currY += num

        elif direction == "L":
            currX -= num

        elif direction == "R":
            currX += num

        point2 = (currX, currY)
        
        for index1, segment in enumerate(segments1):
            is_intersection, intersection_point = get_intersection((point1, point2), segment)

            if is_intersection:
                last_segment1 = get_distance_between_points(intersection_point, segment[0])
                last_segment2 = get_distance_between_points(intersection_point, point1)

                dist_wire1 = get_distance_from_center(index1, instructions1)
                dist_wire2 = get_distance_from_center(index2, instructions2)

                distance = last_segment1 + last_segment2 + dist_wire1 + dist_wire2

                if distance < min_distance:
                    min_distance = distance

    return min_distance

def get_distance_from_center(index, instructions):
    total = 0
    for i in range(index):
        d, num = read_instuction(instructions[i])
        total += num

    return total

def get_distance_between_points(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_segments_wire1(instructions1):
    segments1 = []

    currX = 0
    currY = 0

    for instruction in instructions1:
        point1 = (currX, currY)

        direction, num = read_instuction(instruction)

        if direction == "D":
            currY -= num

        elif direction == "U":
            currY += num

        elif direction == "L":
            currX -= num

        elif direction == "R":
            currX += num

        point2 = (currX, currY)
        segments1.append((point1, point2))

    return segments1

def get_manhattan_distance_from_center(x, y):
    return abs(x) + abs(y)

def get_intersection(coordinates1, coordinates2):
    x11 = coordinates1[0][0]
    y11 = coordinates1[0][1]
    x12 = coordinates1[1][0]
    y12 = coordinates1[1][1]

    x21 = coordinates2[0][0]
    y21 = coordinates2[0][1]
    x22 = coordinates2[1][0]
    y22 = coordinates2[1][1]

    if is_surrounding(x11, x12, x21, x22) and is_surrounding(y21, y22, y11, y12):
        return True, (x21, y11)

    elif is_surrounding(x21, x22, x11, x12) and is_surrounding(y11, y12, y21, y22):
        return True, (x11, y21)

    return False, (0,0)

# Returns true if the first 2 points are before and after the last 2 points
def is_surrounding(x11, x12, x21, x22):
    # If x11 is bigger than x2X and x12 smaller than x2X
    if (x11 > x21 and x11 > x22) and (x12 < x21 and x12 < x22):
        return True
    # If x12 is bigger than x2X and x11 smaller than x2X
    if (x12 > x21 and x12 > x22) and (x11 < x21 and x11 < x22):
        return True

    return False

def read_instuction(instruction):
    direction = instruction[0]
    num = int(instruction[1:])

    return direction, num

run()