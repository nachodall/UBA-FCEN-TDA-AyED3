from collections import deque

class Graph:
    graph = {}
    n = 0
    m = 0
    
    def __init__(self, E):
        for (u,v) in E:
            self.add_edge(u, v)
            
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
            self.n += 1
            
        if v not in self.graph:
            self.graph[v] = []
            self.n += 1
            
        self.graph[v].append(u)
        self.graph[u].append(v)
        self.m += 1
        
from collections import deque

def bfs(g, s):
    q = deque()
    visited = set()  # Use a set to store visited nodes
    q.append(s)
    visited.add(s)
    order = []

    while q:
        v = q.popleft()
        order.append(v)
        neighborhood = g.graph.get(v,[])  # Use the get_neighbors method to get neighbors of v
        for w in neighborhood:
            if w not in visited:
                q.append(w)
                visited.add(w)

    return order

    

