# BFS Traversal Problem

Given a connected undirected graph containing V vertices, represented by a 2-D adjacency list `adj` where `adj[i]` is the list of vertices connected to vertex `i`. Perform a Breadth First Search (BFS) traversal starting from vertex `0`, visiting vertices from left to right according to the order in the given adjacency list, and return a list containing the BFS traversal of the graph.

Note: Traverse neighbors in the same order they appear in the adjacency list.

## Function Signature (Python)

```
def bfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
    pass
```

## Examples

Example 1

Input:

- V = 5
- adj = [[1,2],[0,3],[0,4],[1],[2]]

Output:

- [0, 1, 2, 3, 4]

Explanation: Start at 0 -> visit 1 then 2 (order from adj[0]). From 1 visit 3; from 2 visit 4.

Example 2

Input:

- V = 4
- adj = [[1,2,3],[0],[0],[0]]

Output:

- [0, 1, 2, 3]

Explanation: Start at 0 -> visit 1,2,3 in the order given in `adj[0]`.

---

Implementations should ensure each vertex is visited once and neighbor iteration preserves the adjacency list order.

Example 3

Input:

- adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output:

- [0, 2, 3, 1, 4]

Explanation: Starting from 0, the BFS traversal will follow these steps:
Visit 0 → Output: 0
Visit 2 (first neighbor of 0) → Output: 0, 2
Visit 3 (next neighbor of 0) → Output: 0, 2, 3
Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 1
Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4
