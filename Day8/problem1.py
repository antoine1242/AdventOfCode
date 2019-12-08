import math
import copy

def main():
    with open("input.txt") as f:
        content = f.readline()

    layers = []

    i = 0
    while i < len(content):
        layers.append(content[i:i+150])
        i += 150

    count_max = 1000
    min_layer = -1

    for index, layer in enumerate(layers):
        count = layer.count("0")

        if count < count_max:
            count_max = count
            min_layer = index

    print(layers[min_layer].count("1") * layers[min_layer].count("2"))

main()