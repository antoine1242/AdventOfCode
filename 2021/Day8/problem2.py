def decode_digits(digits):
	digits_dict = {}
	segments_dict = {}

	for digit in digits:
		if len(digit) == 2:
			digits_dict['1'] = digit
		elif len(digit) == 3:
			digits_dict['7'] = digit
		elif len(digit) == 4:
			digits_dict['4'] = digit
		elif len(digit) == 7:
			digits_dict['8'] = digit
	
	for char in digits_dict['7']:
		if char not in digits_dict['1']:
			segments_dict['a'] = char

	digits_lenght_6 = [digit for digit in digits if len(digit) == 6]

	for digit in digits_lenght_6:
		for char in digits_dict['1']:
			if char not in digit:
				digits_dict['6'] = digit
				segments_dict['c'] = char
				segments_dict['f'] = [char for char in digits_dict['1'] if char not in segments_dict['c']][0]

	digits_0_9 = [digit for digit in digits_lenght_6 if digit != digits_dict['6']]
	for digit in digits_0_9:
		for char in digits_dict['4']:
			if char not in digit:
				digits_dict['0'] = digit
				segments_dict['d'] = char
				segments_dict['b'] = [char for char in digits_dict['4'] if char not in digits_dict['0']][0]

	digits_dict['9'] = [digit for digit in digits_0_9 if digit != digits_dict['0']][0]

	digits_lenght_5 = [digit for digit in digits if len(digit) == 5]
	
	digits_dict['5'] = [digit for digit in digits_lenght_5 if segments_dict['c'] not in digit][0]

	segments_dict['e'] = [char for char in digits_dict['6'] if char not in digits_dict['5']][0]

	segments_dict['g'] = [char for char in 'abcdefg' if char not in segments_dict.keys()][0]

	digits_2_3 = [digit for digit in digits if digit not in digits_dict.values()]

	digits_dict['2'] = [digit for digit in digits_2_3 if segments_dict['e'] in digit][0]
	digits_dict['3'] = [digit for digit in digits_2_3 if segments_dict['f'] in digit][0]

	return digits_dict

def decode_output(digits_dict, outputs):
	output_ints = []
	for output in outputs:
		for key, value in digits_dict.items():
			if ''.join(sorted(output)) == ''.join(sorted(value)):
				output_ints.append(key)
	
	return int("".join(output_ints))

def problem1():
	with open("Day8/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines] 

	digits = [x.split("|")[0] for x in lines]
	digits = [digit.split() for digit in digits]

	outputs = [x.split("|")[1] for x in lines]
	outputs = [output.split() for output in outputs]
	
	sum = 0
	for i in range(len(digits)):
		digits_dict = decode_digits(digits[i])
		sum += decode_output(digits_dict, outputs[i])

	return sum
	
print(problem1())