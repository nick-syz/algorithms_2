# https://skillsmart.ru/algo/15-121-cm/x8b3ba28f6.html
# https://skillsmart.ru/algo/15-121-cm/bcb0e51rdc.html

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.hit = False

class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        new_node = Vertex(v)
        self.vertex[self.vertex.index(None)] = new_node
    
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
        self.vertex[VFrom].hit = True
        result.append(self.vertex[VFrom])
        i = 0
        while i < self.max_vertex:
            if self.m_adjacency[VFrom][VTo]:
                result.append(self.vertex[VTo])
                return result
            elif self.m_adjacency[VFrom][i] and not self.vertex[i].hit:
                VFrom = i
                break
            elif i == self.max_vertex-1:
                result.pop()
                if not len(result):
                    return []
                VFrom = len(result)-1
                i = -1
            i += 1
        return self.DepthSearch(VFrom, VTo, result)

    def DepthFirstSearch(self, VFrom, VTo):
        self.MakeDefaultHit()
        return self.DepthSearch(VFrom, VTo, [])
