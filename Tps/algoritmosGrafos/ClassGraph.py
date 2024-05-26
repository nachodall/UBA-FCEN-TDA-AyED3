#undirectional, weighted, simple graphs

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

# Example usage
V = ["A", "B", "C", "D", "E"]
E = [
    ("A", "B", 5),
    ("A", "C", 2),
    ("B", "D", 1),
    ("C", "D", 3),
    ("D", "E", 6),
    ("B", "E", 4),
]

def testGraph():
    graph = Graph(V, E)
    graph.printGraph()

    print("\nDeleting edge B-E")
    graph.deleteEdge("B", "E")
    graph.printGraph()

    print("\nDeleting vertex D")
    graph.deleteVertex("D")
    graph.printGraph()

    print("\nAdding Vertex I")
    graph.addVertex("I")
    graph.addEdge("I", "A", 10)
    graph.printGraph()

    graph.addEdge("B", "I", 4)
    graph.addVertex("J")
    graph.addEdge("I", "J", 7)
    graph.addVertex("M")
    graph.addEdge("S", "M", 10)
    graph.addEdge("M", "D", 8)
    print("\nBFS starting from I")
    graph.bfs("I")
    print("\nDFS starting from I")
    graph.dfs("I")
    set = graph.getVertexSet()
    print(set)
    edfes = graph.getEdgeSet()
    print(edfes)
