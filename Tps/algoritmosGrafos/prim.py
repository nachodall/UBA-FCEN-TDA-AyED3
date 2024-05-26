from ClassGraph import Graph
import heapq

def prim(g: Graph, r):
    mst = Graph(g.getVertexSet(), [])
    visited = [r]
    
    edges = [(r, to, weight) for to, weight in g.adj_list[r]]
    heapq.heapify(edges)
    
    while edges:
        frm, to, weight = heapq.heappop(edges) #take the minimum edge from the nodes i have already visited root
        
        if to not in visited:
            visited.append(to)
            mst.addEdge(frm, to, weight) 
            
            for edge in g.adj_list[to]:
                if edge[0] not in visited:
                    heapq.heappush(edges, (to, edge[0], edge[1])) 
    
    return mst

def test_prim():
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
    mst = prim(g, "A")
    
    # Expected MST edges
    expected_edges = [('A', 'B', 4), ('A', 'H', 8), ('I', 'C', 2), ('H', 'G', 1), ('G', 'F', 2), ('F', 'C', 4), ('C', 'D', 7), ('D', 'E', 9)]
        
    print(mst.getEdgeSet())
    print("arriba mst, abajo expected")
    print(expected_edges)    
    
test_prim()