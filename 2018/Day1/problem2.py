with open("input.txt") as f:
    content = f.readlines()
operations = [x.strip() for x in content]

def main():
    total = 0

    frequency_dict = {}
    frequency_dict[0] = 0

    found = False

    while not found:
        for operation in operations:
            total += get_operation_result(operation)

            if total in frequency_dict:
                print(total)
                found = True
                break
            else:
                frequency_dict[total] = 0

def get_operation_result(operation):
    sign = operation[0]
    num = int(operation[1:])

    if sign == "+":
        return num
    else:
        return -num

main()