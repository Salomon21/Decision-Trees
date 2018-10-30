# -*- coding: utf-8 -*-
import math
from node import Node

def calculate_entropy(node, root, attributes_dict):
	
	values = []
	counter = 0
	entropy = 0.0
	denominator = len(node.dataframe) - 1

	for element in attributes_dict[root.name]:
		counter = 0
		for i in range(1, denominator + 1):
			if element == node.dataframe[i][root.number]:
				counter += 1

		if counter > 0:
			entropy_of_element = - ( (counter/denominator) * math.log(counter/denominator, 2))
		else:
			entropy_of_element = 0
		values.append(entropy_of_element)
	for element in values:
		entropy += element

	return entropy

def information_gain(node, next_node, root, attributes_dict):

	benefit = 0.0
	entropy = 0.0
	values = []
    
	for k in attributes_dict.keys():
		
		if k == next_node.name:
			for datatype in attributes_dict[k]:
				aux_data = []
				aux_data.append(root.dataframe[0])
				for i in range(1, len(next_node.dataframe)):

					if next_node.dataframe[i][next_node.number] == datatype:
						aux_data.append(next_node.dataframe[i])
				new_node = Node(next_node.name, None, None, next_node, next_node.number, aux_data, None, None)
				val = calculate_entropy(new_node, root, attributes_dict)
				val = val * ((len(new_node.dataframe) - 1) / (len(root.dataframe) -1) )

				values.append(val)
			for element in values:
				entropy += element
			benefit = node.entropy - entropy
	return benefit

def find_greater_gain(gains):

	greater = 0.0

	for element in gains:
		if gains[element] > greater:
			greater = gains[element]

	for element in gains:
		if gains[element] == greater:
			return element
