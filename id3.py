# -*- coding: utf-8 -*-
import fileinput
import re
import copy
from entropy import *
from node import Node

def ID3(node, root, attributes_dict, visited):
    
    new_list = copy.deepcopy(visited)
    node.entropy = calculate_entropy(node, root, attributes_dict)
	
    if float(node.entropy) == 0.0:
        node.answer = node.dataframe[1][-1]
        return 0
	
    gains = {}
    for i in range(0, len(node.dataframe[0]) -1):
        if i not in visited:
            next_node = Node(node.dataframe[0][i], None, None, node, i, node.dataframe, None, None)
            gains[node.dataframe[0][i]] = information_gain(node, next_node, root, attributes_dict)

    split_to_node = find_greater_gain(gains)

    new_number = root.dataframe[0].index(split_to_node)
    new_list.append(new_number)

    for element in attributes_dict[split_to_node]:

        new_dataframe = []
        new_dataframe.append(root.dataframe[0])
        new_node = Node(element, None, [], node, new_number, None, None, node.dataframe[0][new_number])
		
        for row in node.dataframe:
            if row[new_number] == element:
                new_dataframe.append(row)
		
        new_node.dataframe = new_dataframe
        node.children.append(new_node)
        ID3(new_node, root, attributes_dict, new_list)
    return 0


def decision_tree(data, attributes_dict):
    
	start = Node(data[0][-1], None, [], None, len(data[0]) -1, data, None, data[0][-1] )
	ID3(start, start, attributes_dict, [])
	start.showTree(-1)
	return 0

if __name__ == "__main__":
    
    #Local tests
    lines = ['@relation or','@attribute A {TRUE, FALSE}','@attribute B {TRUE, FALSE}','@attribute AorB {TRUE, FALSE}','@states',
             'TRUE,TRUE,TRUE','FALSE,FALSE,FALSE','TRUE,FALSE,TRUE','FALSE,TRUE,TRUE']
    
    data = []
    attributes = []
    is_states = False
    states = []
    attributes_dict = {}
    
    for line in lines:
    #for line in fileinput.input():
        if "@attribute" in line:
            words = re.split("[ \t]+|[ \t]+$", line,2)
            attributes.append(words[1])
            words[2] = words[2].replace('{', "")
            words[2] = words[2].replace('}', "")
            words[2] = words[2].replace(' ', "")
            words[2] = words[2].replace('\n', "")
            values = words[2].split(',')
            values_list = []
            for val in values:
                values_list.append(val)
            attributes_dict[words[1]] = values_list
            
        if is_states:
            if not "%" in line:
                new_line = line.replace('\n', "")
                values = new_line.split(',')
                aux = []
                for val in values:
                    aux.append(val)
                states.append(aux)
            
        if "@states" in line:
            is_states = True
            
    data.append(attributes)
    for element in states:
        data.append(element)
    
    decision_tree(data, attributes_dict)