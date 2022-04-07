from collections import deque
import queue


edges = [
    ('w', 'x'),
    ('x', 'y'),
    ('z', 'y'),
    ('z', 'v'),
    ('w', 'v'),
]

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


def shortest_path(graph, source, destination):
    graph = build_graph(edges)
    queue = deque([source])
    visited = set(source[0])

    while(queue):
        node, distance = queue.pop()
        
        if node == destination:
            return distance

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.appendleft((neighbour, distance+1))

    return -1

print(shortest_path(edges, ('w', 0), 'v'))

