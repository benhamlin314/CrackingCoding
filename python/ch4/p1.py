"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 1
 "Route Between Nodes"
 PROMPT:
 Given a directed graph and two nodes (S and E), design an algorithm to find out whether
 there is a route from S to E.
 DATE: 12/10/2019
"""

import unittest
from ch4.queue import Queue
from ch4.graph import Graph, GNode

class PNode(GNode):
    def __init__(self, data):
        super().__init__(data)
        self.discovered = False

def p1(graph: Graph, S: PNode, E: PNode):
    q = Queue()
    S.discovered = True
    q.enqueue(S)
    while not q.isEmpty():
        cur = q.dequeue()
        if cur is E:
            return True
        for child in cur.children:
            if not child.discovered:
                child.discovered = True
                q.enqueue(child)
    return False

class TestP1(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def tearDown(self):
        self.graph = None

    def test_p1(self):
        s = PNode(1)
        a = PNode(2)
        d = PNode(3)
        e = PNode(4)
        s.children.append(a)
        s.children.append(d)
        a.children.append(s)
        a.children.append(d)
        d.children.append(e)
        d.children.append(s)
        e.children.append(s)
        e.children.append(a)
        self.graph.add(s)
        self.graph.add(a)
        self.graph.add(d)
        self.graph.add(e)
        self.assertTrue(p1(self.graph, s, e))
