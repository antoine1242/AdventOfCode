def problem1():
	with open("Day10/input1.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	brackets_dict = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "[", "<": ">", ">": "<"}
	brackets_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
	open_chars = "({[<"
	close_chars = ")}]>"

	score = 0

	for line in lines:
		stack = []

		for char in line:
			if char in open_chars:
				stack.append(char)
			else:
				if stack.pop() != brackets_dict[char]:
					score += brackets_score[char]
					break

	return score
	
print(problem1())