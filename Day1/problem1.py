import math

with open("input1.txt") as f:
    content = f.readlines()
masses = [int(x.strip()) for x in content]

sum = 0

for mass in masses:
	sum += math.floor(mass / 3.) - 2

return sum