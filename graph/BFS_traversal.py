# Breadth First Search (BFS) is a graph traversal algorithm that starts at the root node and explores all the nodes at the current level before moving on to the nodes at the next level.
# BFS is a level order traversal of the graph
# BFS is a recursive algorithm
# BFS is a iterative algorithm
# BFS is a queue based algorithm
# BFS is a tree traversal algorithm
# BFS is a graph traversal algorithm
# BFS is a tree traversal algorithm

#step1: input adjacency list
# input:Number of nodes: 5
# Edges (undirected):
# 0 1
# 0 2
# 1 2
# 1 3
# 2 4
# 3 4


def bfs(n, edges, start):
    # Step 1: Create adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # because undirected graph
    print("Adjacency List:", graph)
    
    # Step 2: Create visited array
    visited = [False] * n
    print("Visited Array:", visited)
    
    # Step 3: Initialize queue
    queue = []
    visited[start] = True
    queue.append(start)
    
    # Step 4: BFS traversal
    print("BFS Traversal Order:")
    while len(queue) > 0:
        node = queue.pop(0)   # dequeue front
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  # enqueue back


def bfs_with_tree_structure(n, edges, start):
    # Step 1: Create adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # because undirected graph
    
    # Step 2: Create visited array and track levels
    visited = [False] * n
    level = {}  # Store level of each node
    parent = {}  # Store parent of each node in BFS tree
    children = {}  # Store children of each node
    
    # Initialize
    for i in range(n):
        children[i] = []
    
    # Step 3: Initialize queue
    queue = []
    visited[start] = True
    level[start] = 0
    parent[start] = None
    queue.append(start)
    
    # Step 4: BFS traversal with tree building
    traversal_order = []
    while len(queue) > 0:
        node = queue.pop(0)
        traversal_order.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                level[neighbor] = level[node] + 1
                parent[neighbor] = node
                children[node].append(neighbor)
                queue.append(neighbor)
    
    return traversal_order, level, parent, children


def print_tree_structure(start, children, level, n):
    """
    Print BFS tree structure in a visual format
    """
    print("\n" + "="*50)
    print("BFS Tree Structure (Level-by-Level):")
    print("="*50)
    
    # Group nodes by level
    nodes_by_level = {}
    for node in range(n):
        if node in level:
            lev = level[node]
            if lev not in nodes_by_level:
                nodes_by_level[lev] = []
            nodes_by_level[lev].append(node)
    
    # Print tree structure level by level
    max_level = max(level.values()) if level else 0
    
    for lev in range(max_level + 1):
        if lev in nodes_by_level:
            print(f"\nLevel {lev}: ", end="")
            nodes = nodes_by_level[lev]
            
            for i, node in enumerate(nodes):
                if lev == 0:
                    print(f"  {node} (root)", end="")
                else:
                    parent_node = None
                    for p in range(n):
                        if node in children.get(p, []):
                            parent_node = p
                            break
                    print(f"  {node}(parent:{parent_node})", end="")
                if i < len(nodes) - 1:
                    print("    ", end="")
            print()
    
    # Print detailed tree structure
    print("\n" + "="*50)
    print("Detailed Tree Structure:")
    print("="*50)
    print_tree_recursive(start, children, "", True, True)
    
    # Print parent-child relationships
    print("\n" + "="*50)
    print("Parent-Child Relationships:")
    print("="*50)
    for node in range(n):
        if node in children and children[node]:
            print(f"Node {node} -> Children: {children[node]}")


def print_tree_recursive(node, children, prefix, is_last, is_root):
    """
    Recursively print tree structure with proper formatting
    """
    if is_root:
        print(f"{node}")
        prefix = ""
    else:
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node}")
        prefix += "    " if is_last else "│   "
    
    child_list = children.get(node, [])
    for i, child in enumerate(child_list):
        is_last_child = (i == len(child_list) - 1)
        print_tree_recursive(child, children, prefix, is_last_child, False)

# ------------------------------
# Example Usage
# ------------------------------
n = 5
edges = [(0,1), (0,2), (1,2), (1,3), (2,4), (3,4)]
start_node = 0

print("="*50)
print("BFS Traversal (Simple):")
print("="*50)
bfs(n, edges, start_node)

print("\n")

# BFS with tree structure visualization
traversal_order, level, parent, children = bfs_with_tree_structure(n, edges, start_node)
print("\nBFS Traversal Order:", traversal_order)
print_tree_structure(start_node, children, level, n)




