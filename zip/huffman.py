print "huff"


class HuffmanNode:
    def __init__(self, val, freq, left=None, right=None):
        self.val = val

        if left is not None and right is not None:
            self.freq = left.freq + right.freq
        else:
            self.freq = freq

        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.list = []

    def add(self, node):
        freq = node.freq
        self.list.append(node)
        index = len(self.list) - 1

        while True:
            parent_index = ((index - 1) / 2)
            parent = self.list[parent_index]

            if parent.freq <= freq:
                break

            temp = node
            self.list[index] = parent
            self.list[parent_index] = temp

            index = parent_index
            if index == 0:
                break

    def size(self):
        return len(self.list)

    def get(self, pos):
        return self.list[pos]

    def pop(self):
        first = self.list[0]

        size = len(self.list)
        self.list[0] = self.list[size - 1]
        del self.list[size - 1]
        index = 0

        while self.size() > 0:

            print "inner", index, "size:", len(self.list)
            current = self.list[index]
            to_change = index

            sub1_index = index * 2 + 1

            if sub1_index <= len(self.list) - 1 and self.list[sub1_index].freq < current.freq:
                current = self.list[sub1_index]
                to_change = sub1_index

            sub2_index = index * 2 + 2

            if sub2_index <= len(self.list) - 1 and self.list[sub2_index].freq < current.freq:
                current = self.list[sub2_index]
                to_change = sub2_index

            if to_change == index:
                break

            temp = self.list[index]
            self.list[index] = current
            self.list[to_change] = temp

            index = to_change
        return first

    def dump(self):
        for i in xrange(0, len(self.list)):
            node = self.list[i]
            print "val %s freq %d" % (node.val, node.freq)


def create_map(str):
    result = {}
    for i in xrange(0, len(str)):
        val = result.get(str[i], 0)
        result[str[i]] = val + 1

    return result


def create_table(node, code, size, map):
    print "create_table", node.val, code, size

    if node.left is not None:
        create_table(node.left, code + "0", size + 1, map)

    if node.right is not None:
        create_table(node.right, code + "1", size + 1, map)

    if node.left is None and node.right is None:
        print "set node", node.val
        map[node.val] = code

def dump_tree(node):
    print "dump tree node.freq", node.freq, node.val

    if node.left is not None:
        dump_tree(node.left)

    if node.right is not None:
        dump_tree(node.right)

def decode(tree, input):
    current = tree

    for c in input:
        if c is "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            print current.val
            current = tree


map = create_map("uuuuuuuuuuuuvvvvvvvvvvvvvvvvvvwwwwwwwxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyy")
queue = Queue()

for (k, v) in map.items():
    node = HuffmanNode(k, v)
    queue.add(node)

queue.dump()

while queue.size() > 1:
    first = queue.pop()
    second = queue.pop()

    newNode = HuffmanNode(0, 0, first, second)
    queue.add(newNode)

result = {}

root = queue.pop()
# dump_tree(root)
create_table(root, "", 0, result)
print result

decode(root, "001011001101")

