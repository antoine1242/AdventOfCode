import math
import copy

Y_COORDINATE = 2000000

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

    impossible_coordinates = set()

    for i in range(len(sensors)):
        # When Y is under
        if Y_COORDINATE >= sensors[i][0]:
            diff = sensors[i][0] + distances[i] - Y_COORDINATE
            if diff >= 0:
                for j in range(sensors[i][1] - diff, sensors[i][1] + diff + 1):
                    if j != beacons[i][1] or beacons[i][0] != Y_COORDINATE:
                        impossible_coordinates.add(j)

        # When Y is above
        else:
            diff = Y_COORDINATE - sensors[i][0] + distances[i]
            if diff >= 0:
                for j in range(sensors[i][1] - diff, sensors[i][1] + diff + 1):
                    if j != beacons[i][1] or beacons[i][0] != Y_COORDINATE:
                        impossible_coordinates.add(j)

    for beacon in beacons:
        if beacon[0] == Y_COORDINATE and beacon[1] in impossible_coordinates:
            impossible_coordinates.remove(beacon[1])

    print(len(impossible_coordinates)) # 5108096

main()
