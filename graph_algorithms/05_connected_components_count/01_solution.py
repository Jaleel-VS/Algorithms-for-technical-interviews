graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}



def count_connected_components(graph):
    count = 0
    visited = set()

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1
    
    return count

def dfs(graph, source, visited):

    visited.add(source)    
    for neighbour in graph[source]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

print(count_connected_components(graph))