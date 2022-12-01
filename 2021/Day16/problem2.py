import numpy as np

def split_packet(binary):
	"""
		Prend un packet principal et renvoie les sous-packets directs qui le composent
	"""
	packets = []

	start = 0
	i = 0

	while i+6 < len(binary):
		curr_type = int(binary[i+3:i+6], 2)

		if curr_type == 4:
			i = i+6
			while binary[i] != "0":
				i += 5
			i += 5

			packets.append(binary[start:i])
			start = i

		else:
			length_type = int(binary[6])

			if length_type == 0:
				length_subpackets = int(binary[7:22], 2)
				packets.append(binary[start:22+length_subpackets])
				i += 22 + length_subpackets

			else:
				nb_subpackets = int(binary[7:18], 2)

				i = i+18
				count_subpackets = 0

				while count_subpackets < nb_subpackets:
					curr_type = int(binary[i+3:i+6], 2)

					if curr_type == 4:
						i = i+6
						while binary[i] != "0":
							i+=5
						i+=5
						count_subpackets += 1
					else:
						raise ValueError("well fuck")

				packets.append(binary[start:i])
				start = i

	return packets

def read_packet(binary):
	"""
		Retourne la valeur si type_id = 4
		Effectue l'opération du type_id sinon
	"""
	if binary[3:6] == "":
		return 0
	type_ID = int(binary[3:6], 2)

	packet_values = []

	if type_ID != 4:
		length_type = int(binary[6], 2)

		if length_type == 0:
			length_subpackets = int(binary[7:22], 2)
			subpackets = split_packet(binary[22:22+length_subpackets])
		else:
			subpackets = split_packet(binary[18:])

		for packet in subpackets:
			if len(packet) > 0:
				packet_values.append(read_packet(packet))

		if type_ID == 0:
			return sum(packet_values)
		elif type_ID == 1:
			return np.prod(packet_values)
		elif type_ID == 2:
			return np.amin(packet_values)
		elif type_ID == 3:
			return np.amax(packet_values)
		elif type_ID == 5:
			return int(packet_values[0] > packet_values[1])
		elif type_ID == 6:
			return int(packet_values[0] < packet_values[1])
		elif type_ID == 7:
			return int(packet_values[0] == packet_values[1])

	else: 
		i = 6

		curr_binary = ""

		while binary[i] != "0":
			curr_binary += binary[i+1:i+5]
			i += 5

		curr_binary += binary[i+1:i+5]

		return int(curr_binary, 2) 

	return 0 

def problem2():
	with open("Day16/input2.txt") as f:
	    packet = f.readline()

	decoded_binary = bin(int(packet, 16))[2:].zfill(len(packet) * 4)
	
	return read_packet(decoded_binary)

print(problem2())