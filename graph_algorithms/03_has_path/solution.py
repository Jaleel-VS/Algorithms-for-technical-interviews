from collections import deque


graph  = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': [],
}

def has_path_dfs(graph, source, destination):
    if source == destination:
        return True
    
    for neighbour in graph[source]:
        return has_path_dfs(graph, neighbour, destination)
        
    return False

def has_path_bfs(graph, source, destination):
    queue = deque([source])
    while(queue):
        current = queue.pop()

        if current == destination:
            return True

        for neighbour in graph[current]:
            queue.appendleft(neighbour)

    return False

if __name__ == "__main__":
    print(has_path_bfs(graph, 'j', 'k'))