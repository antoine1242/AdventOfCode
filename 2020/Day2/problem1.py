def problem1():
	with open("input1.txt") as f:
	    password_rules = f.readlines()
	password_rules = [x.strip() for x in password_rules]

	valid_count = 0

	for password_rule in password_rules:
		rule = password_rule.split(' ')

		count_range = rule[0].split('-')
		letter = rule[1][0]
		password = rule[2]

		letter_count = 0
		for x in range(len(password)):
			if password[x] == letter:
				letter_count += 1

		if letter_count >= int(count_range[0]) and letter_count <= int(count_range[1]):
			valid_count += 1

	return valid_count

print(problem1())