print "huff"

class HuffmanNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

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

    def pop(self):
        first = self.list[0]

        index = 0

        while True:
            sub1_index = index*2 + 1

            if sub1_index > len(self.list) - 1:
                break

            sub2_index = index*2 + 2

            if sub2_index > len(self.list) - 1:
                self.list[index] = self.list[sub2_index]
                break

            if self.list[sub1_index] <= self.list[sub2_index]:
                self.list[index] = self.list[sub1_index]
                index = sub1_index
            else:
                self.list[index] = self.list[sub2_index]
                index = sub2_index

        return first

    def dump(self):
        for i in xrange(0, len(self.list)):
            node = self.list[i]
            print "val %s freq %d"%(node.val, node.freq)





def create_map(str):
    result = {}
    for i in xrange(0, len(str)):
        val = result.get(str[i], 0)
        result[str[i]] = val + 1

    return result


map = create_map("0aabbcccdddd")
queue = Queue()

for (k, v) in map.items():
    node = HuffmanNode(k, v)
    queue.add(node)

queue.dump()

print queue.pop().val
queue.dump()




