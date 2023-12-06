import math
import copy
import re

def find_next(seed, map):
    for rule in map:
        rule = rule.split(" ")
        start_1 = int(rule[0])
        start_2 = int(rule[1])
        range_len = int(rule[2])

        if seed > start_2 and seed < start_2 + range_len:
            return seed - start_2 + start_1
            
    return seed

def main():
    with open("Day5/input.txt") as f:
        lines = f.read().split("\n\n")

    seeds = [int(x) for x in lines[0].split(" ")[1:]]
    seed_to_soil = lines[1].split("\n")[1:]
    soil_to_fertilizer = lines[2].split("\n")[1:]
    fertilizer_to_water = lines[3].split("\n")[1:]
    water_to_light = lines[4].split("\n")[1:]
    light_to_temperature = lines[5].split("\n")[1:]
    temperature_to_humidity = lines[6].split("\n")[1:]
    humidity_to_location = lines[7].split("\n")[1:]

    min_location = 999999999999999999

    for seed in seeds:
        location = find_next(find_next(find_next(find_next(find_next(find_next(find_next(seed, seed_to_soil), soil_to_fertilizer), fertilizer_to_water), water_to_light), light_to_temperature), temperature_to_humidity), humidity_to_location)
        
        if location < min_location:
            min_location = location

    print(min_location)
main()