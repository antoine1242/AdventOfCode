import copy

def problem1():
	with open("Day14/input2.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	first_line = lines[0]

	rules = lines[2:]

	rules = [line.split(" -> ") for line in rules]

	rules_left = [rule[0] for rule in rules]
	rules_right = [rule[1] for rule in rules]
	
	rules_dict = dict(zip(rules_left, rules_right))

	occurences_dict = {}

	for i in range(len(first_line)-1):
		curr_substring = first_line[i] + first_line[i+1]

		if curr_substring in occurences_dict:
			occurences_dict[curr_substring] += 1
		else:
			occurences_dict[curr_substring] = 1

	for i in range(40):
		temp_dict = copy.deepcopy(occurences_dict)

		for key, value in occurences_dict.items():
			temp_dict[key] -= value
			rule_output = rules_dict[key]
			first_substring = key[0] + rule_output

			if first_substring in temp_dict:
				temp_dict[first_substring] += value
			else:
				temp_dict[first_substring] = value

			second_substring =  rule_output + key[1]

			if second_substring in temp_dict:
				temp_dict[second_substring] += value
			else:
				temp_dict[second_substring] = value

		occurences_dict = temp_dict

	char_dict = {}

	for key, value in occurences_dict.items():
		first_char = key[0]

		if first_char in char_dict:
			char_dict[first_char] += value
		else:
			char_dict[first_char] = value

	max_val = 0
	min_val = 999999999999999999

	for key, value in char_dict.items():
		if value > max_val:
			max_val = value
		
		if value < min_val:
			min_val = value

	return max_val - min_val 
	
print(problem1())