class GNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

class Graph(object):
    def __init__(self):
        self.nodes = []

    def add(self, node: GNode):
        self.nodes.append(node)

    def __index__(self, data):
        try:
            index = 0
            while self.nodes[index].data != data:
                index += 1
            return index
        except IndexError:
            raise ValueError("Value not found")
