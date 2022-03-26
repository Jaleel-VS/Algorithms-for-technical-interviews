

def depth_first_print(graph, starting_point):    
    # explicit base case when node is a dead-end
    print(starting_point)
    for neighbour in graph[starting_point]:
        depth_first_print(graph, neighbour)
        

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


depth_first_print(graph, 'a')