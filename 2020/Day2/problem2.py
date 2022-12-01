def problem2():
	with open("input2.txt") as f:
	    password_rules = f.readlines()
	password_rules = [x.strip() for x in password_rules]

	valid_count = 0

	for password_rule in password_rules:
		rule = password_rule.split(' ')

		letter_position = rule[0].split('-')
		letter = rule[1][0]
		password = rule[2]

		if (password[int(letter_position[0]) - 1] == letter) != (password[int(letter_position[1]) - 1] == letter):
			valid_count += 1

	return valid_count

print(problem2())