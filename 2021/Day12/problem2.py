import copy
from collections import Counter

def can_visit(is_big, value, curr_path):
	if is_big:
		return True
	
	if value == "start":
		return False

	if value not in curr_path:
		return True

	counter = Counter(curr_path)

	for k, v in counter.items():
		if k.islower() and v == 2:
			return False

	return True

def find_all_paths(edges, curr_position="start", curr_path=["start"], paths=[]):
	if curr_position == "end":
		paths.append(copy.deepcopy(curr_path))
		curr_path.pop()

		return paths
	
	for i in range(len(edges)):
		for j in range(len(edges[i])):
			if edges[i][j].value == curr_position:
				node_to_visit = edges[i][int(not j)]
				
				if can_visit(node_to_visit.is_big, node_to_visit.value, curr_path):
					curr_path.append(node_to_visit.value)
					paths = find_all_paths(edges, node_to_visit.value, curr_path, paths)

	curr_path.pop()
	return paths

class Node:
	def __init__(self, node):
		self.value = node
		self.is_big = node.isupper()

def problem1():
	with open("Day12/input2.txt") as f:
	    lines = f.read().splitlines() 
	lines = [x.strip("") for x in lines]
	
	edges = [line.split("-") for line in lines]

	vertexes = []
	for edge in edges:
		for i in range(len(edge)):
			is_seen = False
			for vertex in vertexes:
				if vertex.value == edge[i]:
					is_seen = True
					edge[i] = vertex

					break
			if not is_seen:
				new_node = Node(edge[i])
				vertexes.append(new_node)
				edge[i] = new_node

	paths = find_all_paths(edges)

	return len(paths)
	
print(problem1())