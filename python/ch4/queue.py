"""
 CREATED BY: Benjamin Hamlin
 Normal Queue to use for problems in Cracking the Coding Interview
 DATE: 12/11/2019
"""

class Queue(object):
    def __init__(self):
        self._q = []

    def enqueue(self, data):
        self._q.append(data)

    def dequeue(self):
        return self._q.pop(0)

    def isEmpty(self):
        if len(self._q) == 0:
            return True
        return False

    def clear(self):
        self._q.clear()
