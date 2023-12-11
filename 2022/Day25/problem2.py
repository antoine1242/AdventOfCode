import math
import copy

value_dict = {"1": 1, "2": 2, "-": -1, "=": -2, "0": 0}

def main():
    with open("Day25/input.txt") as f:
        lines = f.read().split("\n")

    sum = 0

    for line in lines:
        num = 0
        number = list(line)
        number.reverse()

        for i in range(len(number)):
            num += 5**i * value_dict[number[i]]
        
        sum += num

    print(sum)

    console_input = ""

    i = 0
    while 5**i * 2 < sum:
        i += 1

    while i >= 0:
        if sum > 0:
            if 5**(i-1) > sum:
                console_input += "0"
            elif 5**i * 1 > sum:
                console_input += "1"
                sum -= 5**i * 1
            elif 5**i * 3 > sum:
                console_input += "2"
                sum -= 5**i * 2

        else:
            if -(5**(i-1)) < sum:
                console_input += "0"
            elif -(5**i) * 1 < sum:
                console_input += "-"
                sum += 5**i * 1
            elif -(5**i) * 3 < sum:
                console_input += "="
                sum += 5**i * 2

        i -= 1

    print(console_input)
    
main()
