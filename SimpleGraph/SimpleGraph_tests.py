from SimpleGraph import SimpleGraph
from unittest import TestCase

class SimpleGraphTest(TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

    def test_add(self):
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')
        
        for i in range(5):
            for j in range(5):
                self.assertFalse(self.graph.IsEdge(i, j))
        
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(3, 4)
        
        matrix = [[0, 1, 1, 1, 0], 
                  [1, 0, 0, 1, 1], 
                  [1, 0, 0, 1, 0], 
                  [1, 1, 1, 1, 1], 
                  [0, 1, 0, 1, 0]]
        
        self.assertEqual(matrix, self.graph.m_adjacency)

    def test_remove(self):
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')

        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(3, 4)

        self.graph.RemoveVertex(0)
        matrix = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 1],
                  [0, 1, 0, 1, 0]]
        self.assertEqual(matrix, self.graph.m_adjacency)
        self.assertIsNone(self.graph.vertex[0])

        for i in range(1, 5):
            self.graph.RemoveVertex(i)
            self.assertIsNone(self.graph.vertex[i])

        for i in self.graph.m_adjacency:
            for j in i:
                self.assertFalse(j)

    def test_empty(self):
        # add node in empty graph
        self.graph.AddVertex('A')
        
        # check nothing of endges in the graph
        for i in self.graph.m_adjacency:
            for j in i:
                self.assertFalse(j)

        self.graph.AddVertex('B')
        self.graph.AddEdge(0, 1)

        self.assertTrue(self.graph.m_adjacency[0][1])
        self.assertTrue(self.graph.m_adjacency[1][0])

        self.graph.RemoveEdge(0, 1)

        self.assertFalse(self.graph.m_adjacency[0][1])
        self.assertFalse(self.graph.m_adjacency[1][0])
        
        self.graph.AddEdge(0, 1)
        self.assertTrue(self.graph.m_adjacency[0][1])
        self.assertTrue(self.graph.m_adjacency[1][0])
        self.graph.RemoveVertex(0)

        self.assertFalse(self.graph.m_adjacency[0][1])
        self.assertFalse(self.graph.m_adjacency[1][0])

    def test_depth(self):
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')
        
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        
        res = []
        for i in self.graph.DepthFirstSearch(0, 4):
            res.append(i.Value)

        self.assertFalse(len(res))

        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(3, 4)
        
        res = []
        for i in self.graph.DepthFirstSearch(0, 4):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'E'], res)

        res = []
        for i in self.graph.DepthFirstSearch(0, 1):
            res.append(i.Value)

        self.assertEqual(['A', 'B'], res)

        res = []
        for i in self.graph.DepthFirstSearch(0, 2):
            res.append(i.Value)

        self.assertEqual(['A', 'C'], res)

        res = []
        for i in self.graph.DepthFirstSearch(0, 3):
            res.append(i.Value)

        self.assertEqual(['A', 'D'], res)
    
    def test_breadth(self):
        self.graph.AddVertex('A')
        self.graph.AddVertex('B')
        self.graph.AddVertex('C')
        self.graph.AddVertex('D')
        self.graph.AddVertex('E')

        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        self.graph.AddEdge(0, 3)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(1, 4)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 3)
        self.graph.AddEdge(3, 4) 
        
        res = []
        for i in self.graph.BreadthFirstSearch(0, 2):
            res.append(i.Value)
        
        self.assertEqual(['A', 'C'], res)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 4):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'E'], res)

        self.graph.RemoveEdge(1, 4)
        self.graph.RemoveEdge(3, 4)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 4):
            res.append(i.Value)
    
        self.assertEqual([], res)

        self.graph.RemoveEdge(0, 3)

        res = []
        for i in self.graph.BreadthFirstSearch(0, 3):
            res.append(i.Value)

        self.assertEqual(['A', 'B', 'D'], res)
