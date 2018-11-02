import fileinput
import re
import math
import copy
from node import *
from entropy import *

def ID3(node, root, data_types, visited_list):

	new_list = copy.deepcopy(visited_list)
	node.entropy = calculate_entropy(node, root, data_types)
	#print(node)
	if float(node.entropy) == 0.0:

		#print("LEAF NODE")
		node.answer = node.dataframe[1][-1]
		#print(node.answer)
		return 0
	#print("entropy " + str(node.entropy))
	gains = {}
	#print(node.dataframe)
	for i in range(0, len(node.dataframe[0]) -1):
		if i not in visited_list:
			next_node = Node(node.dataframe[0][i], None, None, node, i, node.dataframe, None, None)
			gains[node.dataframe[0][i]] = information_gain(node, next_node, root, data_types)

	split_to_node = find_greater_gain(gains)

	new_number = root.dataframe[0].index(split_to_node)
	new_list.append(new_number)

	for element in data_types[split_to_node]:

		new_dataframe = []
		new_dataframe.append(root.dataframe[0])
		new_node = Node(element, None, [], node, new_number, None, None, node.dataframe[0][new_number])

		for row in node.dataframe:

			if row[new_number] == element:
				new_dataframe.append(row)

		new_node.dataframe = new_dataframe
		node.children.append(new_node)
		ID3(new_node, root, data_types, new_list)
	return 0


def decision_tree(dataframe, data_types):

	start = Node(dataframe[0][-1], None, [], None, len(dataframe[0]) -1, dataframe, None, dataframe[0][-1] )
	ID3(start, start, data_types, [])
	start.showTree(-1)
	return 0

if __name__ == "__main__":

	dataframe = []
	attributes = []
	data_flag= False
	data = []
	data_types = {}
	for line in fileinput.input():

		if "@attribute" in line:
			words =re.split("[ \t]+|[ \t]+$", line,2)
			#print(words)
			attributes.append(words[1])
			words[2] = words[2].replace('{', "")
			words[2] = words[2].replace('}', "")
			words[2] = words[2].replace(' ', "")
			words[2] = words[2].replace('\n', "")
			#print(words[2])
			values = words[2].split(',')
			values_list = []
			for val in values:
				values_list.append(val)
			data_types[words[1]] = values_list
		if data_flag:

			if not "%" in line:
				new_line = line.replace('\n', "")
				values = new_line.split(',')
				aux_data = []
				for val in values:
					aux_data.append(val)
				data.append(aux_data)

		if "@data" in line:
			data_flag = True
	#print(attributes)
	dataframe.append(attributes)
	for element in data:
		dataframe.append(element)
	decision_tree(dataframe, data_types)
