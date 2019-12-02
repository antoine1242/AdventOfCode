import math

def get_fuel(mass):
    return math.floor(mass / 3.) - 2

with open("input1.txt") as f:
    content = f.readlines()
masses = [int(x.strip()) for x in content]

sum = 0

for mass in masses:
    fuel = get_fuel(mass)

    while(fuel > 0):
        sum += fuel
        fuel = get_fuel(fuel)

print("sum", sum)
