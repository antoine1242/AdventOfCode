def problem1():
	with open("input1.txt") as f:
	    seats = f.readlines()
	seats = [x.strip() for x in seats]

	max_seat_id = 0

	for seat in seats:
		row = seat[:7]
		column = seat[7:]

		row_range = [0, 127]

		for char in row:
			if char == 'F':
				row_range[1] = ((row_range[1] - row_range[0]) // 2) + row_range[0]
			elif char == 'B':
				row_range[0] = ((row_range[1] - row_range[0]) // 2) + 1 + row_range[0]

		row_num = row_range[0]

		column_range = [0, 7]

		for char in column:
			if char == 'L':
				column_range[1] = ((column_range[1] - column_range[0]) // 2) + column_range[0]
			elif char == 'R':
				column_range[0] = ((column_range[1] - column_range[0]) // 2) + 1 + column_range[0]
			
		column_num = column_range[0]

		seat_id = row_num * 8 + column_num

		if seat_id > max_seat_id:
			max_seat_id = seat_id
		
	return max_seat_id

print(problem1())
