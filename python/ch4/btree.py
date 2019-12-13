class BTNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, node: BTNode):
        if self.root is None:
            self.root = node
        else:
            cur = self.root
            while cur is not None:
                if node.data < cur.data:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = node
                        cur = None
                else:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = node
                        cur = None

    def __arrify(self, arr, node: BTNode):
        if node is not None:
            self.__arrify(arr, node.left)
            arr.append(node.data)
            self.__arrify(arr, node.right)

    def arrify(self):
        tarr = []
        self.__arrify(tarr, self.root)
        return tarr
