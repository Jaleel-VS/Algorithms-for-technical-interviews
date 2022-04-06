def depth_first_print(graph, starting_point):
    stack = [starting_point]
    
    assert starting_point in graph

    while len(stack):
        current_val = stack.pop()
        print(current_val)
        for neighbour in graph[current_val]:
            stack.append(neighbour)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


depth_first_print(graph, 'b')