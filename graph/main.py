COLOR_WHITE = 0
COLOR_GREY = 1
COLOR_BLACK = 2


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.list = set([])
        self.color = COLOR_WHITE
        self.hops = -1
        self.route = [value]

    def addNode(self, node):
        self.list.add(node)


node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)
node5 = GraphNode(5)
node6 = GraphNode(6)

node1.addNode(node2)
node1.addNode(node3)

node2.addNode(node1)
node2.addNode(node3)
node2.addNode(node4)

node3.addNode(node1)
node3.addNode(node2)
node3.addNode(node5)

node4.addNode(node2)
node4.addNode(node5)

node5.addNode(node6)

node6.addNode(node5)

graph = [node1, node2, node3, node4, node5, node6]


def bfs(graph, node):
    for n in graph:
        print "find", n.value
        print "current", n.__dict__

        if n is node:
            n.color = COLOR_GREY
            n.hops = 0
        else:
            n.color = COLOR_WHITE
            n.hops = -1

    queue = [node]

    while len(queue) > 0:
        current = queue.pop(0)

        current.color = COLOR_BLACK

        for nextNode in current.list:
            if nextNode.color == COLOR_WHITE:
                nextNode.color = COLOR_GREY
                nextNode.hops = current.hops + 1
                nextNode.route += current.route
                queue.append(nextNode)

    for n in graph:
        print n.value, "", n.hops, n.route


# bfs(graph, node1)

cs100 = GraphNode("cs100")
cs200 = GraphNode("cs200")
cs300 = GraphNode("cs300")
ma100 = GraphNode("ma100")
ma200 = GraphNode("ma200")
ma300 = GraphNode("ma300")
cs150 = GraphNode("cs150")

cs100.addNode(cs200)
cs200.addNode(cs300)
cs300.addNode(ma300)
ma100.addNode(ma200)
ma100.addNode(cs300)
ma200.addNode(ma300)

graph2 = [cs100, cs200, cs300, ma100, ma200, ma300, cs150]


def dfs_main(node, list, order):
    node.color = COLOR_GREY
    for n in list:
        if n.color == COLOR_WHITE:
            dfs_main(n, n.list, order)

    node.color = COLOR_BLACK
    order.append(node)


def dfs(graph, order):
    for n in graph:
        n.color = COLOR_WHITE

    for n in graph:
        if n.color == COLOR_WHITE:
            dfs_main(n, n.list, order)


order = []
dfs(graph2, order)

for n in order:
    print n.value