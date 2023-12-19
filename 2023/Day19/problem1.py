from aocd.models import Puzzle
import copy
from enum import Enum
import parse
import time

DAY = 19

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n\n")

    rules = ls[0].split("\n")
    parts = ls[1].split("\n")

    rules_dict = {}

    for rule in rules:
        rule_name = rule.split("{")[0]

        rules_dict[rule_name] = rule.split("{")[1].split("}")[0].split(",")

    sum_parts = 0

    for part in parts:
        curr = part.split(",")
        x = int(curr[0].split("=")[1].strip())
        m = int(curr[1].split("=")[1].strip())
        a = int(curr[2].split("=")[1].strip())
        s = int(curr[3].split("=")[1].split("}")[0].strip())

        curr_rule = "in"

        in_rule = True
        while in_rule:
            if curr_rule == "A":
                sum_parts += x+m+a+s
                in_rule = False
                break
            elif curr_rule == "R":
                in_rule = False
                break

            for workflow in rules_dict[curr_rule]:
                if workflow == "A":
                    sum_parts += x+m+a+s
                    in_rule = False
                    break
                elif workflow == "R":
                    in_rule = False
                    break

                elif isinstance(workflow, str) and workflow in rules_dict:
                    curr_rule = workflow
                    break

                letter = workflow[0]
                comparator = workflow[1]
                num = int(workflow[2:].split(":")[0])
                new_rule = workflow[2:].split(":")[1]

                if letter == "a":
                   letter_value = a
                elif letter == "x":
                    letter_value = x
                elif letter == "m":
                    letter_value = m 
                elif letter == "s":
                    letter_value = s 

                if comparator == ">":
                    if letter_value > num:
                        curr_rule = new_rule
                        break
                    else:
                        continue
                else:
                    if letter_value < num:
                        curr_rule = new_rule
                        break
                    else:
                        continue
        
    print(sum_parts)
    
#main(test=True)
main() # 532551
