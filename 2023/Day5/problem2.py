import math
import copy
import numpy as np
import re

def merge_ranges(ranges):
    # Step 1: Sort the list of ranges based on the start of each range
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    # Step 2: Merge overlapping ranges
    merged_ranges = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_merged_range = merged_ranges[-1]

        # Check for overlap
        if current_range[0] <= last_merged_range[1]:
            # Merge ranges
            last_merged_range[1] = max(last_merged_range[1], current_range[1])
        else:
            # No overlap, add the current range to the result
            merged_ranges.append(current_range)

    return merged_ranges

def find_limits(seeds_ranges, map): 
    new_ranges = []
    while len(seeds_ranges) > 0:
        added = False
        temp_ranges = []
        for range in seeds_ranges:
            range_rule_found = False
            for index, rule in enumerate(map):
                rule = rule.split(" ")
                start_map = int(rule[0])
                start_seed = int(rule[1])
                range_len = int(rule[2])

                diff = start_map - start_seed
                end_seed = start_seed + range_len - 1 

                if range[0] >= start_seed and range[0] <= end_seed and range[1] >= end_seed:
                    range_rule_found = True
                    new_ranges.append([range[0]+diff, end_seed+diff])
                    if range[1] > end_seed:
                        temp_ranges.append([end_seed+1, range[1]])
                        added = True        
                                                                    
                elif range[0] >= start_seed and range[0] <= end_seed and range[1] <= end_seed:
                    range_rule_found = True                                                         # seeds_range 79 14 55 13  -> 79 - 92    55 - 67                                                                                           
                    new_ranges.append([range[0] + diff, range[1] + diff])                           # map 50 98 2              -> 98-99 = 50-51 => Rien                                                               # 52 50 48                 -> 50-97 = 52-99 => 81-94   57-69  
            
                elif range[0] <= start_seed and range[1] >= start_seed and range[1] <= end_seed:
                    range_rule_found = True
                    if range[0] <  start_seed:
                        temp_ranges.append([range[0], start_seed-1])
                        added = True
                    new_ranges.append([start_seed + diff, range[1] + diff])
                                    
                elif range[0] <= start_seed and range[1] >= end_seed:
                    range_rule_found = True
                    if range[0] <  start_seed:
                        temp_ranges.append([range[0], start_seed-1])
                        added = True
                    new_ranges.append([start_seed + diff, end_seed + diff])
                    if range[1] > end_seed:
                        temp_ranges.append([end_seed+1, range[1]])
                        added = True
                
                elif index == len(map) - 1 and not range_rule_found:
                    temp_ranges.append(range)

        if added:
            seeds_ranges = copy.deepcopy(temp_ranges)
        elif seeds_ranges == temp_ranges:
            return seeds_ranges
        elif len(temp_ranges) == 0 and len(new_ranges) == 0:
            return seeds_ranges
        else:
            new_ranges = new_ranges + temp_ranges
            seeds_ranges = []

    new_ranges = merge_ranges(new_ranges)
            
    return new_ranges

def main():
    with open("Day5/input.txt") as f:
        lines = f.read().split("\n\n")

    seeds_ranges = [int(x) for x in lines[0].split(" ")[1:]]
    seeds_ranges = [seeds_ranges[i:i+2] for i in range(0, len(seeds_ranges), 2)]
    seeds_ranges = [[seeds_range[0], seeds_range[0] + seeds_range[1]-1] for seeds_range in seeds_ranges]
    
    maps = []
    for i in range(1, len(lines)):
        maps.append(lines[i].split("\n")[1:])

    for map in maps:
        seeds_ranges = find_limits(seeds_ranges, map)

    seeds_ranges = np.array(seeds_ranges).ravel()

    print(min(seeds_ranges))    #6472060
    
main()
