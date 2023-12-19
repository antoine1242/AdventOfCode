from aocd.models import Puzzle
import copy
from enum import Enum
import parse
import time

DAY = 19

def rule_passes(x,m,a,s,rules_dict):
    curr_rule = "in"

    in_rule = True
    while in_rule:
        if curr_rule == "A":
            return True

        elif curr_rule == "R":
            return False

        for workflow in rules_dict[curr_rule]:
            if workflow == "A":
                return True
            elif workflow == "R":
                return False

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

def get_passes_total(rules_dict, x_values, m_values, a_values, s_values, current_rule):
    if current_rule == "A":
        return (x_values[1]-x_values[0]+1) * (m_values[1]-m_values[0]+1) * (a_values[1]-a_values[0]+1) * (s_values[1]-s_values[0]+1)
    elif current_rule == "R":
        return 0
    
    total = 0
    for workflow in rules_dict[current_rule]:
        if workflow == "R":
            continue
        elif workflow == "A":
            total += (x_values[1]-x_values[0] + 1) * (m_values[1]-m_values[0] + 1) * (a_values[1]-a_values[0] + 1) * (s_values[1]-s_values[0] + 1)
        elif len(workflow) <= 3:
            total += get_passes_total(rules_dict, x_values, m_values, a_values, s_values, workflow)
        else:
            workflow_letter = workflow[0]
            comparator = workflow[1]
            workflow_num = int(workflow[2:].split(":")[0])
            new_rule_name = workflow[2:].split(":")[1]

            if workflow_letter == "x":
                if comparator == "<":
                    total += get_passes_total(rules_dict, [x_values[0], workflow_num-1], m_values, a_values, s_values, new_rule_name)
                    x_values = [workflow_num, x_values[1]]
                else:
                    total += get_passes_total(rules_dict, [workflow_num+1, x_values[1]], m_values, a_values, s_values, new_rule_name)
                    x_values = [x_values[0], workflow_num]
            elif workflow_letter == "m":
                if comparator == "<":
                    total += get_passes_total(rules_dict, x_values, [m_values[0], workflow_num-1], a_values, s_values, new_rule_name)
                    m_values = [workflow_num, m_values[1]]
                else:
                    total += get_passes_total(rules_dict, x_values, [workflow_num+1, m_values[1]], a_values, s_values, new_rule_name)
                    m_values = [m_values[0], workflow_num]
            elif workflow_letter == "a":
                if comparator == "<":
                    total += get_passes_total(rules_dict, x_values, m_values, [a_values[0], workflow_num-1], s_values, new_rule_name)
                    a_values = [workflow_num, a_values[1]]
                else:
                    total += get_passes_total(rules_dict, x_values, m_values, [workflow_num+1, a_values[1]], s_values, new_rule_name)
                    a_values = [a_values[0], workflow_num]
            elif workflow_letter == "s":
                if comparator == "<":
                    total += get_passes_total(rules_dict, x_values, m_values, a_values, [s_values[0], workflow_num-1], new_rule_name)
                    s_values = [workflow_num, s_values[1]]
                else:
                    total += get_passes_total(rules_dict, x_values, m_values, a_values, [workflow_num+1, s_values[1]], new_rule_name)
                    s_values = [s_values[0], workflow_num]
    
    return total

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n\n")

    rules = ls[0].split("\n")
    rules_dict = {}

    for rule in rules:
        rule_name = rule.split("{")[0]

        rules_dict[rule_name] = rule.split("{")[1].split("}")[0].split(",")

    x_values = [1, 4000]
    m_values = [1, 4000]
    a_values = [1, 4000]
    s_values = [1, 4000]

    passes = get_passes_total(rules_dict, x_values, m_values, a_values, s_values, 'in')

    print(passes)

#main(test=True)
main() # 134343280273968
