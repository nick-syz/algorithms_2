# https://skillsmart.ru/algo/15-121-cm/x8b3ba28f6.html
# https://skillsmart.ru/algo/15-121-cm/bcb0e51rdc.html
# https://skillsmart.ru/algo/15-121-cm/f827a03dcc.html
# https://skillsmart.ru/algo/15-121-cm/e2b325a2cf.html

import queue

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False
        self.index = None

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        new_node = Vertex(v)
        i = self.vertex.index(None)
        new_node.index = i
        self.vertex[i] = new_node
        
    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(len(self.m_adjacency[v])):
            if self.IsEdge(v, i):
                self.RemoveEdge(v, i)

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] and self.m_adjacency[v2][v1]:
            return True
        return False
	
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
    
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def MakeDefaultHit(self):
        for node in self.vertex:
            node.hit = False
    
    def DepthSearch(self, VFrom, VTo, result):
        if not self.vertex[VFrom].hit:
            self.vertex[VFrom].hit = True
            result.append(self.vertex[VFrom])
            if self.m_adjacency[VFrom][VTo]:
                result.append(self.vertex[VTo])
                return result
        for i in range(self.max_vertex):
            if self.m_adjacency[VFrom][i] and not self.vertex[i].hit:
                return self.DepthSearch(i, VTo, result)
        result.pop()
        if not len(result):
            return []
        return self.DepthSearch(len(result)-1, VTo, result)

    def DepthFirstSearch(self, VFrom, VTo):
        self.MakeDefaultHit()
        return self.DepthSearch(VFrom, VTo, [])
    
    def BSearch(self, VTo, queue, prev):
        if not queue.qsize():
            return []
        VFrom = queue.get().index
        for i in range(self.max_vertex):
            if self.m_adjacency[VFrom][i]:
                if not self.vertex[i].hit:
                    queue.put(self.vertex[i])
                    self.vertex[i].hit = True
                    prev.append(self.vertex[VFrom])
                if i == VTo:
                    prev.append(self.vertex[VTo])
                    return prev
        return self.BSearch(VTo, queue, prev)
    
    def MakePath(self, prev):
        path = []
        for i in range(1, len(prev)):
            if prev[i] != prev[i-1]:
                path.append(prev[i-1])
            if i == len(prev)-1:
                path.append(prev[i])
        return path

    def BreadthFirstSearch(self, VFrom, VTo):
        self.MakeDefaultHit()
        q = queue.Queue()
        q.put(self.vertex[VFrom])
        self.vertex[VFrom].hit = True
        prev = self.BSearch(VTo, q, [])
        return self.MakePath(prev)
    
    def MakeGraphDict(self, matrix):
        graph = {}
        for i in range(len(matrix)):
            graph[i] = []
            for j in range(len(matrix)):
                if matrix[i][j]:
                    graph[i].append(j)
        return graph
    
    def WeakVertices(self):
        self.MakeDefaultHit()
        graph = self.MakeGraphDict(self.m_adjacency)
        for i in range(self.max_vertex):
            for j in graph[i]:
                for k in graph[i]:
                    if j != k:
                        if k in graph[j]:
                            self.vertex[i].hit = True
        result = []
        for node in self.vertex:
            if not node.hit:
                result.append(node)
        return result
