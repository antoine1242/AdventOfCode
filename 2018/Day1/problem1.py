def main():
    with open("input.txt") as f:
    content = f.readlines()
    operations = [x.strip() for x in content]

    total = 0

    for operation in operations:
        total += get_operation_result(operation)

    print(total)


def get_operation_result(operation):
    sign = operation[0]
    num = int(operation[1:])

    if sign == "+":
        return num
    else:
        return -num

main()