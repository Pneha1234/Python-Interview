# unweighted, undirected graph 
# Number of nodes: 5
# Number of edges: 6

# Edges:
# 0 1
# 0 2
# 1 2
# 1 3
# 2 4
# 3 4

# Unweighted, undirected graph

# Step 1 : create a matrix of size n*n
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

# Step 2 : fill the matrix with edges
def fill_matrix_with_edges(matrix, edges):
    for edge in edges:
        u = edge[0]
        v = edge[1]
        matrix[u][v] = 1
        matrix[v][u] = 1   # because undirected
    return matrix

# Step 3 : print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Step 4 : create and fill matrix
def create_and_fill_matrix(n, edges):
    matrix = create_matrix(n)
    fill_matrix_with_edges(matrix, edges)
    return matrix

create_and_fill_matrix(5, [(0,1), (0,2), (1,2), (1,3), (2,4), (3,4)])
