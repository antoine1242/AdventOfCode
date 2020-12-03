import math
import copy

def main():
    with open("input.txt") as f:
        entries = f.readlines()

    transactions = []

    for entry in entries:
        transactions.append(extract_transaction(entry))

    low = 0
    high = 2000000
    while low < high:
        print(low)
        print(high)
        mid = (low + high) // 2
        req = get_ressources("FUEL", mid, transactions, {})
        if req > 1000000000000:
            high = mid - 1
        elif req < 1000000000000:
            low = mid
    
    print(low)
    print(mid)
    print(high)


def get_ressources(element_name, element_number, transactions, available_ressources):
    curr_transaction = None

    # Find the transaction to create element_name
    for transaction in transactions:
        if transaction.output_element == element_name:
            curr_transaction = transaction
            break
    
    total_ores = 0
    available_global = 0
    if curr_transaction.output_element in available_ressources:
        available_global = available_ressources[curr_transaction.output_element]

    while available_global < element_number:
        # For each input
        for i in range(len(curr_transaction.input_elements)):
            if curr_transaction.input_elements[i] == "ORE":
                total_ores += curr_transaction.input_numbers[i]
                if curr_transaction.output_element in available_ressources:
                    available_ressources[curr_transaction.output_element] += curr_transaction.output_number
                else:
                    available_ressources[curr_transaction.output_element] = curr_transaction.output_number
                if curr_transaction.output_element in available_ressources:
                    available_global = available_ressources[curr_transaction.output_element]
            else:
                available = 0
                if curr_transaction.input_elements[i] in available_ressources:
                    available = available_ressources[curr_transaction.input_elements[i]]
                # While you don't have enough of this input
                while available < curr_transaction.input_numbers[i]:
                    total_ores += get_ressources(curr_transaction.input_elements[i], curr_transaction.input_numbers[i], transactions, available_ressources)

                    if curr_transaction.input_elements[i] in available_ressources:
                        available = available_ressources[curr_transaction.input_elements[i]]

                # Remove from available and create ressource
                if curr_transaction.input_elements[0] != "ORE":
                    available_ressources[curr_transaction.input_elements[i]] -= curr_transaction.input_numbers[i]

        if curr_transaction.input_elements[0] != "ORE":
            if curr_transaction.output_element in available_ressources:
                available_ressources[curr_transaction.output_element] += curr_transaction.output_number
            else:
                available_ressources[curr_transaction.output_element] = curr_transaction.output_number         

        if curr_transaction.output_element in available_ressources:
            available_global = available_ressources[curr_transaction.output_element]

    return total_ores

def extract_transaction(entry):
    reaction = entry.split(" => ")

    output = reaction[1].split(" ")
    output_number = int(output[0])
    output_element = output[1].strip("\n")

    inputs = reaction[0].split(", ")
    input_elements = []
    input_numbers = []

    for input_ in inputs:
        curr = input_.split(" ")
        input_numbers.append(int(curr[0]))
        input_elements.append(curr[1])

    return Transaction(input_elements, input_numbers, output_element, output_number)

class Transaction:
    def __init__(self, input_elements, input_numbers, output_element, output_number):
        self.input_elements = input_elements
        self.input_numbers = input_numbers
        self.output_element = output_element
        self.output_number = output_number

    def __str__(self):
        return str(self.input_elements) + str(self.input_numbers) + str(self.output_element) + str(self.output_number)

main()