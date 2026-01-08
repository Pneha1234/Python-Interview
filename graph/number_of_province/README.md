# Number of Provinces

## Problem Statement

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the ith city and the jth city are directly connected, and `isConnected[i][j] = 0` otherwise.

**Return the total number of provinces.**

## Function Signature

```python
def findCircleNum(isConnected: List[List[int]]) -> int:
    pass
```

## Examples

### Example 1

**Input:**
```
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
```

**Output:**
```
2
```

**Explanation:** Cities 0 and 1 form one province, and city 2 forms another province.

### Example 2

**Input:**
```
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
```

**Output:**
```
3
```

**Explanation:** Each city forms a separate province.

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`
- `isConnected[i][i] == 1` (a city is connected to itself)
- `isConnected[i][j] == isConnected[j][i]` (the matrix is symmetric)

## Approach

This problem can be solved using:
- **Depth First Search (DFS):** Visit each unvisited city and explore all directly/indirectly connected cities
- **Breadth First Search (BFS):** Similar to DFS but using a queue
- **Union-Find (Disjoint Set Union):** Group cities into connected components

Each approach will count the number of connected components in the graph.

---

**Topics:** Graph, DFS, BFS, Union-Find  
**Difficulty:** Medium  
**Acceptance Rate:** ~69.7%
