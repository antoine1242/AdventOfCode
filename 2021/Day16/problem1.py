def split_packet(binary):
	packets = []

	start = 0
	i = 0

	finished = False
	while not finished:
		curr_type = int(binary[i+3:i+6], 2)

		if curr_type == 4:
			i += 6
			while binary[i] != '0':
				i += 5

			i += 5

			packets.append(binary[start:i])
			start = i

		else:
			i += 6
			if binary[i] == '0':
				length_subpackets = int(binary[i+1:i+16], 2)
				i = i + 16 + length_subpackets
				packets.append(binary[start:i])
				start = i
			else:
				packets.append(binary[start:])
				finished = True

		if i + 6 > len(binary):
			finished = True

	return packets

def read_packet(binary):
	if len(binary) == 0:
		return 0

	versions = int(binary[:3], 2)

	type_ID = int(binary[3:6], 2)

	if type_ID != 4:
		length_type = int(binary[6], 2)

		if length_type == 0:
			length_subpackets = int(binary[7:22], 2)
			subpackets = split_packet(binary[22:22+length_subpackets])
		else:
			number_of_subpackets = int(binary[7:18], 2)
			subpackets = split_packet(binary[18:])

		for packet in subpackets:
			versions += read_packet(packet)		

	return versions	

def problem1():
	with open("Day16/input1.txt") as f:
	    packet = f.readline()

	decoded_binary = bin(int(packet, 16))[2:].zfill(len(packet) * 4)
	versions_total= read_packet(decoded_binary)
	
	return versions_total

print(problem1())