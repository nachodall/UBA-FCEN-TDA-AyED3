#https://vjudge.net/problem/UVA-1235

class Graph: 
    def __init__(self, V, E):
        self.adj_list = {}
        for v in V:
            self.addVertex(v)
        
        for u, v, weight in E:
            self.addEdge(u, v, weight)
        
    def addVertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def addEdge(self, u, v, weight):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
            
    def deleteEdge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u] = [(w, weight) for w, weight in self.adj_list[u] if w != v]
            self.adj_list[v] = [(w, weight) for w, weight in self.adj_list[v] if w != u]
    
    def deleteVertex(self, v):
        if v in self.adj_list:
            # Remove all edges associated with the vertex
            for neighbor, _ in self.adj_list[v]:
                self.adj_list[neighbor] = [(w, weight) for w, weight in self.adj_list[neighbor] if w != v]
            # Remove the vertex itself
            del self.adj_list[v]
    
    def getVertexSet(self):
        return [v for v in self.adj_list]
 
    def getEdgeSet(self):
        edgeSet = []
        for v in self.adj_list:
            for edge in self.adj_list[v]:
                if (edge[0], v, edge[1]) not in edgeSet:
                    edgeSet.append((v,edge[0],edge[1]))
        return edgeSet
    
    def isEdge(self,v,w):
        if v not in self.adj_list or w not in self.adj_list:
            return False 
        
        for u,_ in self.adj_list[v]:
            if u == w: return True 
            
        return False
    
    def bfs(self, r):
        queue = [r]
        visited = set()
        
        while queue:
            current = queue.pop(0)  
            if current not in visited:
                visited.add(current)
                print(current)
                for neighbor, _ in self.adj_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return visited
    
    def dfs(self,r):
        stack = [r]
        visited = set()
        
        while stack:
            current = stack.pop()  
            if current not in visited:
                visited.add(current)
                print(current)
                for neighbor, _ in self.adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    
    def printGraph(self):
        for v in self.adj_list:
            print(f"{v}: {self.adj_list[v]}")
            
class DisjSet: 
    def __init__(self): 
        # Constructor to create and initialize sets
        self.rank = {}
        self.parent = {}

    # Make a new set with a single item
    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    # Finds set of given item x
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 

    # Do union of two sets represented by x and y
    def union(self, x, y): 
        self.link(self.find(x), self.find(y))
        
    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

def kruskal(g: Graph):
    mst = Graph(g.getVertexSet(), [])
    edges = sorted(g.getEdgeSet(), key=lambda edge: edge[2])
    ds = DisjSet()
    
    for v in g.getVertexSet():
        ds.make_set(v)
        
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.addEdge(u, v, weight)
            ds.union(u, v)
    
    return mst

def rollsRequiered(key1, key2):
    res = 0
    if len(key1) != len(key2): return -1
    
    for i in range(len(key1)-1,-1,-1): 
        print('entre')
        digit1 = int(key1[i])
        print(digit1)
        digit2 = int(key2[i])
        print(digit2)
        res += abs(digit1 - digit2)
    
    return res 


def solve(n, keys):
    G = Graph(keys, [])
    
    for i in range(n-1): #first i add the edges supposing i don't have the JUMP button
        weightFromNodeToNode = rollsRequiered(keys[i], keys[i+1])
        weightFromZeroToNode = rollsRequiered('0000', keys[i+1])
        weight = min(weightFromNodeToNode, weightFromZeroToNode)
        G.addEdge(keys[i], keys[i+1], weight)
    
    for i in range(n-1): #now i add the JUMP functionality, which implies that every vertex is conected to every vertex, converting G in a Kn-type graph
        for j in range(n-1):
            if i != j and not G.isEdge(keys[i], keys[j]):
                weight = rollsRequiered(keys[i], keys[j])
                G.addEdge(keys[i], keys[j], weight)
            
    mst = kruskal(G)
    
    totalCost = sum(weight for _,_,weight in mst.getEdgeSet())
    
    return totalCost
        


