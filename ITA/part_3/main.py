#coding:utf-8
print "二叉树相关"

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

        if left is not None:
            left.parent = self

        if right is not None:
            right.parent = self

def middle_visit(tree):
    if tree is None:
        return

    middle_visit(tree.left)
    print tree.value
    middle_visit(tree.right)

def search_tree(tree, x):
    while tree is not None and tree.value != x:
        if x < tree.value:
            tree = tree.left
        else:
            tree = tree.right

    if tree is not None:
        return tree.value
    else:
        return "not found"

def tree_min(tree):
    while tree.left != None:
        tree = tree.left

    return tree

def tree_successor(tree):
    if tree.right is not None:
        return tree_min(tree.right)
    else:
        y = tree.parent

        while y is not None and tree is y.right:
            tree = tree.parent
            y = tree.parent

        return y

def tree_insert(tree, node):
    x = tree
    y = None

    while x is not None:
        y = x
        if node.value < x.value:
            x = y.left
        else:
            x = y.right

    node.parent = y

    if node.value < y.value:
        y.left = node
    else:
        y.right = node




#create a tree

node9 = Node(9, None, None)
node13 = Node(13, node9, None)
node7 = Node(7, None, node13)
node2 = Node(2, None, None)
node4 = Node(4, None, None)
node3 = Node(3, node2, node4)
node6 = Node(6, node3, node7)
node17 = Node(17, None, None)
node20 = Node(20, None, None)
node18 = Node(18, node17, node20)
node15 = Node(15, node6, node18)

# middle_visit(node15)
# print search_tree(node15, 99)
# print tree_min(node7).value
node16 = Node(16, None, None)

tree_insert(node15, node16)
middle_visit(node15)
