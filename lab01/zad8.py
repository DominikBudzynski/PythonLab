import unittest
from zad7 import Node

class TestNode(unittest.TestCase):    
    def test_treeTraverse(self):
        root = Node(1)
        child1 = Node(2)
        child2 = Node(3)

        root.addChildren(child1)
        root.addChildren(child2)
        child1.addChildren(Node(21))
        child1.addChildren(Node(22))
        child2.addChildren(Node(31))
        child2.addChildren(Node(32))       

        result = []

        expectedResult = [
            "11",
            "\t2",
            "\t\t21",
            "\t\t22",
            "\t3",
            "\t\t31",
            "\t\t32"
        ]
 
        def mock_generateOutput(node, num):
            result.append('\t' * num + str(node.value))
        
        root.treeTraverse(mock_generateOutput)

        self.assertEqual(result, expectedResult, "THERE IS A DIFFERENCE BETWEEN OUTPUTS")                    

if __name__ == '__main__':
    unittest.main()