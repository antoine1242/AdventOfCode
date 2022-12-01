def extract_fields(passport):

	fields_whole = passport[1:].split(' ')

	fields = []

	for field in fields_whole:
		fields.append(field.split(':')[0])

	return fields


def problem1():
	with open("input1.txt") as f:
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

	for passport in passports_separated:
		valid = True

		fields = extract_fields(passport)

		for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
			if field not in fields:
				print(passport)
				print(field)
				valid = False
				break

		if valid:
			valids += 1

	return valids

print(problem1())
