import numpy as np

def main():
    with open("input.txt") as f:
        content = f.readline()

    layers = []

    i = 0

    while i < len(content):
        layers.append([])
        for j in range(6):
            layers[int(i/150)].append(content[i:i+25])
            i += 25

    output = np.full((6, 25), 2)
    for i in range(len(layers)):
        for m in range(6):
            for n in range(25):
                if output[m,n] == 2:
                    output[m,n] = layers[i][m][n]

    print(output)

main()