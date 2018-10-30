# -*- coding: utf-8 -*-
class Node:
	def __init__(self, name, entropy, children, father, number, dataframe, answer, column):
		self.entropy = entropy
		self.name = name
		self.children = children
		self.father =  father
		self.number = number
		self.dataframe = dataframe
		self.answer = answer
		self.column = column

	def setEntropy(self, ent):
		self.entropy = ent

	def setChildren(self, newChild):
		self.children.append(newChild)

	def setFather(self, newFather):
		self.father = newFather

	def showTree(self, spaces):
		if self.name != self.dataframe[0][-1]:
			print("  " * spaces + self.column + ": " +self.name)
		if self.answer:
			print ("  " * spaces + "  " +  "ANSWER: " + self.answer)
		for child in self.children:
			child.showTree(spaces + 1)