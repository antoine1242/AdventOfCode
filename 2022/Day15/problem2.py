import math
import copy

MAX_Y = 4000000

def merge_ranges(ranges):
    # Step 1: Sort the list of ranges based on the start of each range
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    # Step 2: Merge overlapping ranges
    merged_ranges = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_merged_range = merged_ranges[-1]

        # Check for overlap
        if current_range[0] <= last_merged_range[1]+1:
            # Merge ranges
            last_merged_range[1] = max(last_merged_range[1], current_range[1])
        else:
            # No overlap, add the current range to the result
            merged_ranges.append(current_range)

    return merged_ranges

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def main():
    with open("Day15/input.txt") as f:
        lines = f.read().split("\n")

    sensors = [[int(value) for value in array] for array in [line.split(":")[0].split("x=")[1].split(", y=") for line in lines]]
    sensors = [[sensor[1], sensor[0]] for sensor in sensors]
    beacons = [[int(value) for value in array] for array in [line.split(":")[1].split("x=")[1].split(", y=") for line in lines]]
    beacons = [[beacon[1], beacon[0]] for beacon in beacons]
    distances = [manhattan(sensors[i], beacons[i]) for i in range(len(sensors))]

    ranges = [[] for i in range(MAX_Y+1)]

    for index, sensor in enumerate(sensors):
        print("Sensor:", sensor)
        for i in range(sensor[0] - distances[index], sensor[0] + distances[index] + 1):
            if i >= 0 and i <= MAX_Y: 
                if i <= sensor[0]:
                    diff = abs(sensor[0] - (i + distances[index]))
                else:
                    diff = abs(i - sensor[0] - distances[index])

                ranges[i].append([max(sensor[1]-diff, 0), min(sensor[1]+diff, MAX_Y)])
    new_ranges = []
    for x in ranges:
        new_ranges.append(merge_ranges(x))

    for i in range(len(new_ranges)):
        if len(new_ranges[i]) > 1:
            return (new_ranges[i][0][1] + 1) * 4000000 + i

print(main())


    # for i in range(1, MAX_Y + 1):
    #     print(i)
    #     for j in range(MAX_Y + 1):
    #         distress = True
    #         for k in range(len(sensors)):
    #             if manhattan([i,j], sensors[k]) <= distances[k]:
    #                 distress = False
    #                 break
    #         if distress:
    #             for k in range(len(beacons)):
    #                 if beacons[k][0] == i and beacons[k][1] == j:
    #                     distress = False
    #                     break
    #         if distress:
    #             return 4000000 * j + i

    # for y in range(MAX_Y + 1):
    #     if y % 1000 == 0:
    #         print(y)

    #     impossible_coordinates = set()

    #     for i in range(len(sensors)):
    #         # When Y is under
    #         if y >= sensors[i][0]:
    #             diff = sensors[i][0] + distances[i] - y
    #             if diff >= 0:
    #                 for j in range(sensors[i][1] - diff, sensors[i][1] + diff + 1):
    #                     if (j != beacons[i][1] or beacons[i][0] != y) and j >= 0 and j <= MAX_Y:
    #                         impossible_coordinates.add(j)

    #         # When Y is above
    #         else:
    #             diff = y - sensors[i][0] + distances[i]
    #             if diff >= 0:
    #                 for j in range(sensors[i][1] - diff, sensors[i][1] + diff + 1):
    #                     if (j != beacons[i][1] or beacons[i][0] != y) and j >= 0 and j <= MAX_Y:
    #                         impossible_coordinates.add(j)
        
    #     for beacon in beacons:
    #         if beacon[0] == y and beacon[1] >= 0 and beacon[1] <= MAX_Y:
    #             impossible_coordinates.add(beacon[1])

    #     if len(impossible_coordinates) < MAX_Y + 1:
    #         for coord in range(MAX_Y + 1):
    #             if coord not in impossible_coordinates:
    #                 return coord * 4000000 + y 