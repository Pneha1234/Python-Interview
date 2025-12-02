#An adjacency list stores a graph as:
# A list (or dict) where
# Each node stores a list of its neighbors

def create_adjacency_list(n, edges):
    adjacency_list = []
    for i in range(n):
        adjacency_list.append([])
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        # if its a weighted graph, then we can use the weight of the edge
        # adjacency_list[u].append((v, weight))
        # adjacency_list[v].append((u, weight))
    return adjacency_list

print(create_adjacency_list(5, [(0,1), (0,2), (1,2), (1,3), (2,4), (3,4)]))

def create_adjacency_dict(n, edges):
    adjacency_dict = {}
    for i in range(n):
        adjacency_dict[i] = []
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adjacency_dict[u].append(v)
        adjacency_dict[v].append(u)
    return adjacency_dict

print(create_adjacency_dict(5, [(0,1), (0,2), (1,2), (1,3), (2,4), (3,4)]))