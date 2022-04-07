# converts an edge list to an adjency list
import pprint

def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph
   
def has_path_dfs(graph, source, destination, visited: set[str]):
    if source == destination:
        return True

    if source in visited:
        return False

    visited.add(source)
    
    for neighbour in graph[source]:
        if has_path_dfs(graph, neighbour, destination, visited):
            return True
        
    return False