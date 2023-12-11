import math
import copy

value_dict = {"1": 1, "2": 2, "-": -1, "=": -2, "0": 0}

def convert_to_snafu(number):
    console_input = ""

    i = 0
    while 5**i * 2 + math.ceil(5**(i) / 2) - 1 < number:
        i += 1

    while i >= 0:
        if number >= 0:
            if number == 0 and i == 0:
                console_input += "0"
            elif number == 1 and i == 0:
                console_input += "1"
                number -= 1
            elif number == 2 and i == 0:
                console_input += "2"
                number -= 1
            elif 5**(i-1) * 2 >= number:
                console_input += "0"
            elif 5**i + (math.ceil(5**i / 2) - 1) >= number:
                console_input += "1"
                number -= 5**i * 1
            else:
                console_input += "2"
                number -= 5**i * 2

        else:
            if number == -1 and i == 0:
                console_input += "-"
                number += 1
            elif number == -2 and i == 0:
                console_input += "="
                number += 1
            elif -(5**(i-1)) * 2 <= number:
                console_input += "0"
            elif (-(5**i)) + -(math.ceil(5**i / 2) - 1) <= number:
                console_input += "-"
                number += 5**i
            else:
                console_input += "="
                number += 5**i * 2

        i -= 1

    return console_input

def conver_to_decimal(snafu):
    num = 0
    number = list(snafu)
    number.reverse()

    for i in range(len(number)):
        num += 5**i * value_dict[number[i]]

    return num

def main():
    with open("Day25/input.txt") as f:
        lines = f.read().split("\n")

    total = 0

    for line in lines:
        total += conver_to_decimal(line)

    print(total)
    snafu = convert_to_snafu(total)
    print(snafu) # 20-==01-2-=1-2---1-0
    print(conver_to_decimal(snafu))

main()
