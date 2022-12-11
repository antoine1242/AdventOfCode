import math
import copy

def calc_new_worry(item, op, op_value):
    if op_value == "old":
        op_value = item
    else:
        op_value = int(op_value)
    
    if op == "+":
        return item + op_value
    elif op == "*":
        return item * op_value
    else:
        print("ERROR")

def test_worry(new_worry, test):
    return new_worry % test == 0

def main():
    with open("Day11/input.txt") as f:
        monkeys = f.read().split("\n\n")

    monkeys_items = [[int(value) for value in array] for array in [monkey.split("\n")[1].split(": ")[1].split(", ") for monkey in monkeys]]
    monkeys_op = [monkey.split("\n")[2].split(" ")[-2] for monkey in monkeys]
    monkeys_op_value = [monkey.split("\n")[2].split(" ")[-1] for monkey in monkeys]
    monkeys_test = [int(monkey.split("\n")[3].split(" ")[-1]) for monkey in monkeys]
    monkeys_true = [int(monkey.split("\n")[4].split(" ")[-1]) for monkey in monkeys]
    monkeys_false = [int(monkey.split("\n")[5].split(" ")[-1]) for monkey in monkeys]
    monkey_throws = [0 for i in range(len(monkeys))]

    for i in range(10000):
        for j in range(len(monkeys)):

            for item in monkeys_items[j]:
                new_worry = calc_new_worry(item, monkeys_op[j], monkeys_op_value[j]) 
                new_worry = new_worry % math.prod(monkeys_test)
                test_result = test_worry(new_worry, monkeys_test[j])

                if test_result:
                    monkeys_items[monkeys_true[j]].append(new_worry)
                else:
                    monkeys_items[monkeys_false[j]].append(new_worry)

                monkey_throws[j] += 1

            monkeys_items[j] = []

    monkey_throws.sort()

    print(monkey_throws[-1] * monkey_throws[-2])

main()