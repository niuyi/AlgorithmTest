import random


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.factor = 0

    def insert(self, node):
        if node.value < self.value:
            self.factor += 1
            if self.left is not None:
                self.left.insert(node)
            else:
                self.left = node

        if node.value > self.value:
            self.factor -= 1
            if self.right is not None:
                self.right.insert(node)
            else:
                self.right = node


def getNode(node):
    if node is None:
        return "none"
    else:
        return node.value


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node):
        self.size += 1
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

        if self.root.factor > 1:
            left = self.root.left
            grandChild = left.right

            if left.factor >= 1:
                print "do LL"

                self.root.factor = 0
                left.factor = 0

                self.root.left = left.right
                left.right = self.root
                self.root = left
            else:
                print "do LR"
                left.right = grandChild.left
                grandChild.left = left
                self.root.left = grandChild.right
                grandChild.right = self.root
                self.root = grandChild

        if self.root.factor < -1:
            right = self.root.right
            grandChild = right.left

            if right.factor <= -1:
                print "do RR"

                self.root.factor = 0
                right.factor = 0

                self.root.right = right.left
                right.left = self.root
                self.root = right
            else:
                print "do RL"
                right.left = grandChild.right
                grandChild.right = right
                self.root.right = grandChild.left
                grandChild.left = self.root
                self.root = grandChild

    def leftVisit(self, node):
        if node.left is not None:
            self.leftVisit(node.left)

        print node.value, getNode(node.left), getNode(node.right)

        if node.right is not None:
            self.leftVisit(node.right)

    def visit(self):
        print "root: ", self.root.value
        self.leftVisit(self.root)


init_list = [10, 11, 25, 27, 29, 30, 34, 45, 59, 20]
random.shuffle(init_list)

# init_list = [1,3,2]

tree = Tree()

for i in init_list:
    print i
    node = Node(i, None, None)
    tree.insert(node)

print "after insert"

tree.visit()
