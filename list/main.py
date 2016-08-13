class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyList:

    def __init__(self):
        self.count = 0
        self.header = None

    def insert(self, node):
        self.count += 1
        if self.header is None:
            self.header = node
        else:
            node.next = self.header
            self.header = node

    def visit(self):
        current = self.header
        while current is not None:
            print current.value
            current = current.next

l = MyList()
node = MyNode(1)
l.insert(node)
l.insert(MyNode(200))
l.insert(MyNode(300))
print l.count
l.visit()
