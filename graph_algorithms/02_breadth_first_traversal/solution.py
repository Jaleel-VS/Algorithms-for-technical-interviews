from collections import deque

def breadth_first_print(graph, starting_point):
    assert starting_point in graph

    queue = deque([starting_point])
    
    while len(queue):
        current_val = queue.pop()
        print(current_val)
        for neighbour in graph[current_val]:
            queue.appendleft(neighbour)
        

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


breadth_first_print(graph, 'a')