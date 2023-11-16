
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

    @property
    def minTreeValue(self):
        def minValue(self):
            value = self.value
            for child in self.children:
                value = min(value, minValue(child))
            return value
        return minValue(self)
    
root = Node(10)
child1 = Node(5)
child2 = Node(8)
child3 = Node(12)

root.addChildren(child1)
root.addChildren(child2)
root.addChildren(child3)

child1.addChildren(Node(1))
child2.addChildren(Node(7))
child3.addChildren(Node(15))

print(root.minTreeValue)