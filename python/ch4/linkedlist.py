class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.list = None

    def add(self, data):
        if self.list is not None:
            cur = self.list
            while cur.next is not None:
                cur = cur.next
            cur.next = LLNode(data)
        else:
            self.list = LLNode(data)
