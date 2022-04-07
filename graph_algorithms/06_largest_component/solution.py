def largest_component(graph):
    biggest = -1

    visited = set()

    for node in graph:
        if node not in visited:
            size = dfs(graph, node, visited)

            if size > biggest:
                biggest = size
    
    return biggest

def dfs(graph, source, visited):
    if source in visited:
        return 0
    visited.add(source)

    size = 1
    for neighbour in graph[source]:
            size += dfs(graph, neighbour, visited)
    
    return size

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(largest_component(graph))