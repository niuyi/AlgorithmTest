import sys
import math

COLOR_WHITE = 0
COLOR_GREY = 1
COLOR_BLACK = 2


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.list = {}
        self.color = COLOR_WHITE
        self.weight = sys.maxint
        self.parent = None
        self.d = sys.maxint

    def addNode(self, node, weight):
        self.list[node] = weight


a = GraphNode("a")
b = GraphNode("b")
c = GraphNode("c")
d = GraphNode("d")
e = GraphNode("e")
f = GraphNode("f")

a.addNode(b, 8)
a.addNode(c, 4)

b.addNode(c, 6)
b.addNode(d, 2)

c.addNode(f, 1)
c.addNode(e, 4)

e.addNode(f, 5)

f.addNode(b, 2)
f.addNode(d, 7)
f.addNode(e, 4)

my_graph = [a, b, c, d, e, f]


def mst(graph, start):
    for node in graph:
        if node is start:
            node.weight = 0

    size = len(graph)
    i = 0

    while i < size:
        current_node = None
        current_min = sys.maxint

        for node in graph:
            if node.color is COLOR_WHITE and node.weight < current_min:
                current_node = node
                current_min = current_node.weight

        current_node.color = COLOR_BLACK
        print "find smallest node", current_node.value

        for key in current_node.list:
            current_weight = key.weight
            weight = current_node.list[key]

            if weight < current_weight:
                key.weight = weight
                key.parent = current_node

        i += 1

    for node in graph:
        if node.parent is not None:
            print "node:%s weight:%d parent:%s color:%d" % (node.value, node.weight, node.parent.value, node.color)


def shortest(graph, start):
    for node in graph:
        if node is start:
            node.d = 0

    size = len(graph)
    i = 0

    while i < size:
        current_node = None
        current_min = sys.maxint

        for node in graph:
            if node.color is COLOR_WHITE and node.d < current_min:
                current_node = node
                current_min = current_node.d

        current_node.color = COLOR_BLACK
        # print "find smallest node", current_node.value

        for key in current_node.list:
            if current_node.d + current_node.list[key] < key.d:
                key.d = current_node.d + current_node.list[key]
                key.parent = current_node

        i += 1

    for node in graph:
        if node.parent is not None:
            print "node:%s d:%d parent:%s color:%d" % (node.value, node.d, node.parent.value, node.color)


# mst(my_graph, a)

shortest(my_graph, a)


class TripNode:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.color = COLOR_WHITE

a = TripNode("a", 2, 1)
b = TripNode("b", 5, 2)
c = TripNode("c", 1, 3)
d = TripNode("d", 4, 3)
e = TripNode("e", 6, 3)
f = TripNode("f", 2, 4)
g = TripNode("g", 5, 5)

my_graph = [a, b, c, d, e, f, g]


def tsp(graph, start):
    result = [start]

    while len(result) is not len(graph):
        current = result[len(result) - 1]
        current.color = COLOR_BLACK

        dis = sys.maxint
        next_node = None
        for node in graph:
            if node.color is COLOR_WHITE:
                this_dis = math.sqrt((node.x - current.x)**2 + (node.y - current.y)**2)
                if this_dis <= dis:
                    dis = this_dis
                    next_node = node

        result.append(next_node)

    result.append(start)

    for node in result:
        print node.value

tsp(my_graph, a)

