import unittest

class Node:

    def __init__(self, element):

        self.left = None
        self.right = None
        self.element = element


class BinaryTree:

    def __init__(self):

        self.root = None


    def insert(self, element):

        self.root = self.insertAux(element, self.root)

        return self.root


    def insertAux(self, element, node):

        if (node == None):

            return Node(element)

        compareResult = 0

        if (element < node.element):

            compareResult = -1

        elif (element > node.element):

            compareResult = 1

        if (compareResult < 0):

            node.left = self.insertAux(element, node.left)

        elif (compareResult > 0):

            node.right = self.insertAux(element, node.right)

        return node


    def remove(self, element):

        self.root = self.removeAux(element, self.root)

        return self.root


    def removeAux(self, element, node):

        if (node == None):

            return None

        compareResult = 0

        if (element < node.element):

            compareResult = -1

        elif (element > node.element):

            compareResult = 1

        elif (element == node.element):

            compareResult = 0

        if (compareResult < 0):

            node.left = self.removeAux(element, node.left)

        elif (compareResult > 0):

            node.right = self.removeAux(element, node.right)

        elif (node.left != None and node.right != None):

            node.element = self.findMin(node.right).element
            node.right = self.removeAux(node.element, node.right)

        else:

            node = node.right

        return node


    def findMin(self, node):

        if (node == None):

            return None

        elif (node.left == None):

            return node

        else:

            return self.findMin(node.left)


    def findMax(self, node):

        if (node == None):

            return None

        elif (node.right == None):

            return node

        else:

            return self.findMax(node.right)


    def inOrder(self, node):

        if (node != None):

            self.inOrder(node.left)
            print(node.element)
            self.inOrder(node.right)


    def preOrder(self, node):

        if (node != None):

            print(node.element)
            self.preOrder(node.left)
            self.preOrder(node.right)


    def postOrder(self, node):

        if (node != None):

            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.element)


binaryTree = BinaryTree()

print("min")
print(binaryTree.findMin(binaryTree.root))
print("")

print("max")
print(binaryTree.findMax(binaryTree.root))
print("")

binaryTree.insert(5)
binaryTree.insert(2)
binaryTree.insert(-4)
binaryTree.insert(-7)
binaryTree.insert(1)
binaryTree.insert(3)
binaryTree.insert(12)
binaryTree.insert(9)
binaryTree.insert(21)
binaryTree.insert(19)
binaryTree.insert(25)

print("inOrder")
binaryTree.inOrder(binaryTree.root)
print("")

print("preOrder")
binaryTree.preOrder(binaryTree.root)
print("")

print("postOrder")
binaryTree.postOrder(binaryTree.root)
print("")

print("min")
print(binaryTree.findMin(binaryTree.root).element)
print("")

print("max")
print(binaryTree.findMax(binaryTree.root).element)
print("")

print("remove 12")
binaryTree.remove(12)
print("")

print("remove 20")
binaryTree.remove(20)
print("")

print("remove 55")
binaryTree.remove(55)


class Test_BinaryTree(unittest.TestCase):

    def test_insert(self):

        self.assertEqual(binaryTree.insert(5),binaryTree.root)

    def test_remove(self):

        self.assertEqual(binaryTree.remove(5),binaryTree.root)

    def test_findMin(self):

        self.assertEqual(binaryTree.findMin(binaryTree.root).element,-7)

    def test_findMax(self):

        self.assertEqual(binaryTree.findMax(binaryTree.root).element,25)


if __name__ == "__main__":

    unittest.main()
