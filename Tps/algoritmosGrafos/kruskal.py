from ClassGraph import Graph
from disjointSet import DisjSet

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

def test_kruskal():
    # Create a graph (Example of Cormen's book)
    g = Graph([],[])
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for vertex in vertices:
        g.addVertex(vertex)
    
    edges = [('A', 'B', 4), ('A', 'H', 8), ('B', 'C', 8), ('B', 'H', 11), ('F', 'C', 4),
             ('H', 'I', 7), ('H', 'G', 1), ('G', 'F', 2), ('I', 'G', 6), ('I', 'C', 2), ('C', 'D', 7), ('C', 'F', 4), ('D', 'F', 14), ('D', 'E', 9), ('E', 'F', 10)]
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])
    
    # Perform Kruskal's algorithm
    mst = kruskal(g)
    
    # Expected MST edges
    expected_edges = [('A', 'B', 4), ('A', 'H', 8), ('I', 'C', 2), ('H', 'G', 1), ('G', 'F', 2), ('F', 'C', 4), ('C', 'D', 7), ('D', 'E', 9)]
        
    print(mst.getEdgeSet())
    print("arriba mst, abajo expected")
    print(expected_edges)    
    
test_kruskal()