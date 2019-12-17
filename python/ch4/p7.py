"""
 CREATED BY: Benjamin Hamlin
 Chapter 4 Question 7
 "Build Order"
 PROMPT:
 You are given a list of projects and a list of dependencies (which is a list of
 pairs of projects, where the second project is dependent on the first project)
 All of a project's dependencies must be built before the project is. Find a
 build order that will allow the projects to be built. If there is no valid build
 order return an error
 DATE: 12/13/2019
"""

import unittest
from ch4.graph import Graph, GNode
from ch4.queue import Queue

class PNode(GNode):
    def __init__(self, data):
        super().__init__(data)
        self.discovered = False
        self.isTraversed = False

def p7(projects, dependencies):
    # Build Graph
    g = Graph()
    dep = []
    for p in projects:
        g.add(PNode(p))
    for p, d in dependencies:
        loc = g.__index__(p)
        deploc = g.__index__(d)
        g.nodes[loc].children.append(g.nodes[deploc])
        dep.append(d)
    count_abs = 0
    for p in projects:
        if p not in dep:
            count_abs += 1

    buildOrder = []
    q = Queue()
    while len(buildOrder) != len(projects) - count_abs:
        for p in g.nodes:
            # reset traversal
            q.clear()
            for d in g.nodes:
                d.discovered = False
            # DFS
            if not p.isTraversed and p.data in dep:
                q.enqueue(p)
                while not q.isEmpty():
                    cur = q.dequeue()
                    if len(cur.children) == 0 and not cur.isTraversed:
                        # Leaf is found
                        cur.isTraversed = True
                        buildOrder.insert(0, cur.data)
                        break
                    for child in cur.children:
                        if child.isTraversed:
                            cur.children.remove(child)
                        if not child.discovered and not cur.isTraversed:
                            child.discovered = True
                            q.enqueue(child)
            else:
                g.nodes.remove(p)

    # add nondependent to front
    for p in projects:
        if p not in dep:
            buildOrder.insert(0,p)
            pass

    return buildOrder

class TestP7(unittest.TestCase):
    def test_p7(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
        self.assertEqual(p7(projects,dependencies),['f','e','a','b','d','c'])
