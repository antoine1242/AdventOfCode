from aocd.models import Puzzle

DAY = 15

def main(test=False):
    if test:
        with open(f"Day{DAY}/input.txt") as f:
            ls = f.read()
    else:
        ls = Puzzle(year=2023, day=DAY).input_data

    ls = ls.split("\n")

    operations = ls[0].split(",")

    total = 0
    for op in operations:
        temp = 0
        for char in op:
            temp += ord(char)
            temp *= 17
            temp = temp % 256

        total += temp
    print(total)

#main(test=True)
main() # 512283
