# DFS Traversal Problem

Given a connected undirected graph containing V vertices, represented by a 2-D adjacency list `adj` where `adj[i]` is the list of vertices connected to vertex `i`. Perform a Depth First Search (DFS) traversal starting from vertex `0`, visiting vertices from left to right according to the order in the given adjacency list, and return a list containing the DFS traversal of the graph.

Note: Traverse neighbors in the same order they appear in the adjacency list.

## Function Signature (Python)

```
def dfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
    pass
```

## Example

Input:

- adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output:

- [0, 2, 4, 3, 1]

Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 2 (the first neighbor of 0) → Output: 0, 2
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

---

Implementations should ensure each vertex is visited once and neighbor iteration preserves the adjacency list order.
