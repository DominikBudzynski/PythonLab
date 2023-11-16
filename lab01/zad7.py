import unittest

class Node:
    def __init__(self):
        self.value = 0

    def __init__(self, value):
        self.value = value
        self.children = []

    def addChildren(self, node):
        self.children.append(node)

    def __str__(self):
        return str(self.value) + "\n"
    
    def treeTraverse(self, visitingFun, num = 0):
        visitingFun(self, num)    
        for child in self.children:                        
            child.treeTraverse(visitingFun, num + 1)

root = Node(1)
child1 = Node(2)
child2 = Node(3)

def printNode(node, num):
    print('\t' * num + str(node.value))

root.addChildren(child1)
root.addChildren(child2)

child1.addChildren(Node(21))
child1.addChildren(Node(22))
child2.addChildren(Node(31))
child2.addChildren(Node(32))

root.treeTraverse(printNode)
