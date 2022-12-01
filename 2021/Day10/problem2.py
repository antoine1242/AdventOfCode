def problem2():
	with open("Day10/input2.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]

	brackets_dict = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "[", "<": ">", ">": "<"}
	brackets_score = {")": 1, "]": 2, "}": 3, ">": 4}
	open_chars = "({[<"
	close_chars = ")}]>"

	scores = []

	for line in lines:
		line_score = 0
		stack = []
		corrupted = False

		for char in line:
			if char in open_chars:
				stack.append(char)
			else:
				if stack.pop() != brackets_dict[char]:
					corrupted = True
					break

		if not corrupted:
			for char in reversed(stack):
				close_bracket = brackets_dict[char]
				line_score = (line_score * 5) + brackets_score[close_bracket]
		
			scores.append(line_score)

	scores.sort()

	return scores[len(scores)//2]
	
print(problem2())