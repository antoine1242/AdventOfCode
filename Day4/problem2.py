import re

def extract_fields(passport):

	fields_whole = passport[1:].split(' ')

	fields = []

	for field in fields_whole:
		fields.append(field.split(':')[0])

	return fields

def extract_values(passport):

	fields_whole = passport[1:].split(' ')

	fields = []

	for field in fields_whole:
		fields.append(field.split(':'))

	return fields

def check_validity(values):
	for entry in values:
		if entry[0] == 'byr':
			if len(entry[1]) != 4 or int(entry[1]) < 1920 or int(entry[1]) > 2002:
				return False

		elif entry[0] == 'iyr':
			if len(entry[1]) != 4 or int(entry[1]) < 2010 or int(entry[1]) > 2020:
				return False

		elif entry[0] == 'eyr':
			if len(entry[1]) != 4 or int(entry[1]) < 2020 or int(entry[1]) > 2030:
				return False

		elif entry[0] == 'hgt':
			if entry[1][-2:] == 'cm':
				if int(entry[1][:-2]) < 150 or int(entry[1][:-2]) > 193:
					return False

			elif entry[1][-2:] == 'in':
				if int(entry[1][:-2]) < 59 or int(entry[1][:-2]) > 76:
					return False

		elif entry[0] == 'hcl':
			pattern = re.compile("^[a-f0-9]{6,}$")
			if entry[1][0] != '#' or not pattern.match(entry[1][1:]):
				return False

		elif entry[0] == 'ecl':
			if len(entry[1]) != 3 or entry[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				return False

		elif entry[0] == 'pid':
			if len(entry[1]) != 9 or not entry[1].isnumeric():
				return False

	return True

def problem2():
	with open("input2.txt") as f:
	    passports = f.readlines()
	passports = [x.strip() for x in passports]

	passports_separated = ['']

	i = 0
	
	for x in range(len(passports)):
		if passports[x] == '':
			i += 1
			passports_separated.append('')
		else:
			passports_separated[i] = passports_separated[i] + ' ' + passports[x]

	valids = 0
	invalids = 0

	for passport in passports_separated:
		valid = True

		fields = extract_fields(passport)
		values = extract_values(passport)

		for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
			if field not in fields:
				valid = False
				break

		if valid:
			valid = check_validity(values)

		if valid:
			valids += 1
		else:
			invalids += 1

	return valids

print(problem2())
