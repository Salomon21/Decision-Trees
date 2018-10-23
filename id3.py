# -*- coding: utf-8 -*-
import fileinput
import re

if __name__ == "__main__":
    
    #Local tests
    lines = ['@relation or','@attribute A {TRUE, FALSE}','@attribute B {TRUE, FALSE}','@attribute AorB {TRUE, FALSE}','@states',
             'TRUE,TRUE,TRUE','FALSE,FALSE,FALSE','TRUE,FALSE,TRUE','FALSE,TRUE,TRUE']
    
    data = []
    attributes = []
    is_states = False
    states = []
    attributes_dict = {}
    
    #for line in lines:
    for line in fileinput.input():
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
    
    print(attributes)
    print("\n")
    print(data)
    print("\n")
    print(states)
    print("\n")
    print(attributes_dict)
    print("\n")