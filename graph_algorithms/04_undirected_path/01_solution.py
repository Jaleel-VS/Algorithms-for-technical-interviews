from helper import build_graph, has_path_dfs
from pprint import pprint

def undirected_path(edges, nodeA, nodeB):
    graph = build_graph(edges)

    return has_path_dfs(graph, nodeA, nodeB, set())

# edges =  [(0,1), (0,6), (0,8), (1,4), (1,6), (1,9), (2,4), (2,6), (3,4), (3,5),
# (3,8), (4,5), (4,9), (7,8), (7,9) ]

edges = [
     ['i', 'j'],
     ['k', 'i'],
     ['m', 'k'],
     ['k', 'l'],
     ['o', 'n'],
 ]

print(undirected_path(edges, 'n', 'i'))

