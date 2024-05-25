from ClassGraph import Graph
from disjointSet import DisjSet

def kruskal(g: Graph):
    mst = Graph(g.getVertexSet(), [])
    edges = sorted(g.getEdgeSet(), key=lambda edge:edge[2]) # here's where the greedy magic happens, we always look the minimum weighted edge
    ds = DisjSet()
    
    for v in mst.adj_list: 
        ds.make_set(v) 
        
    for u,w,weight in edges:
        if ds.find(w) != ds.find(u):
            mst.addEdge(u,w,weight)
            ds.union(w,u)
    
    return mst

def test_kruskal():
    # Create a graph
    g = Graph([],[])
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    for vertex in vertices:
        g.addVertex(vertex)
    
    edges = [('A', 'B', 4), ('A', 'F', 2), ('B', 'C', 6), ('B', 'F', 5),
             ('C', 'D', 3), ('C', 'F', 8), ('D', 'E', 7), ('D', 'F', 1), ('E', 'F', 9)]
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])
    
    # Perform Kruskal's algorithm
    mst = kruskal(g)
    
    # Expected MST edges
    expected_edges = [('A', 'F', 2), ('D', 'F', 1), ('C', 'D', 3), ('A', 'B', 4), ('B', 'F', 5)]
    
    print(mst.getEdgeSet())
    print("arriba mst, abajo expected")
    print(expected_edges)    
    
test_kruskal()