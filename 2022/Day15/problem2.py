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

print(main()) # 10553942650264