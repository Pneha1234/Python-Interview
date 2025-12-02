# Graph Basics

## What is a Graph?

A **graph** is a mathematical structure used to represent relationships between objects. It consists of:

- **Nodes (Vertices)**: The objects or entities in the graph, typically represented as circles or points.
- **Edges**: The connections or relationships between nodes, typically represented as lines or arcs.

Graphs are widely used in computer science to model various real-world scenarios such as:
- Social networks (people as nodes, friendships as edges)
- Transportation networks (cities as nodes, roads as edges)
- Web pages (pages as nodes, links as edges)
- Dependency relationships (tasks as nodes, dependencies as edges)

**Notation**: A graph is typically denoted as G = (V, E), where:
- V is the set of vertices (nodes)
- E is the set of edges

---

## Nodes (Vertices)

**Nodes**, also called **vertices**, are the fundamental units of a graph. They represent entities, objects, or data points in the system being modeled.

**Characteristics**:
- Each node can store data or attributes
- Nodes can be labeled or unlabeled
- The number of nodes in a graph is called the **order** of the graph

**Example**: In a social network graph, each person is a node. In a city map graph, each intersection is a node.

---

## Edges

**Edges** are the connections between nodes in a graph. They represent relationships, links, or interactions between the entities represented by nodes.

**Types of Edges**:
1. **Undirected Edge**: A connection that has no direction (bidirectional relationship)
   - Represented as a line between two nodes: A — B
   - If there's an edge between A and B, you can travel from A to B and from B to A

2. **Directed Edge**: A connection that has a direction (one-way relationship)
   - Represented as an arrow: A → B
   - If there's a directed edge from A to B, you can only travel from A to B, not the other way

3. **Self-loop**: An edge that connects a node to itself
   - Represented as an arc: A ↻

4. **Multiple edges**: Multiple edges between the same pair of nodes
   - Also called parallel edges

**Edge Properties**:
- Edges can have **weights** (numerical values representing cost, distance, capacity, etc.)
- Edges can have labels or attributes
- The number of edges in a graph is called the **size** of the graph

---

## Directed Graph

A **directed graph** (also called a **digraph**) is a graph where all edges have a direction.

**Characteristics**:
- Edges are ordered pairs: if there's an edge from A to B, it's different from an edge from B to A
- Represented as arrows: A → B
- Direction matters: if you have A → B, you can travel from A to B but not necessarily from B to A

**Example**: 
- Web pages: Page A links to Page B (A → B), but Page B might not link back to Page A
- Dependency graphs: Task A must complete before Task B (A → B)
- Food chain: Species A is eaten by Species B (A → B)

**Notation**: G = (V, E) where E contains ordered pairs (u, v) indicating an edge from u to v.

---

## Undirected Graph

An **undirected graph** is a graph where edges have no direction.

**Characteristics**:
- Edges are unordered pairs: if there's an edge between A and B, it's the same as an edge between B and A
- Represented as lines: A — B
- Bidirectional: if there's an edge between A and B, you can travel from A to B and from B to A

**Example**:
- Social networks: If A is friends with B, then B is friends with A
- Road networks: A road between City A and City B can be traveled in both directions
- Molecular structures: Chemical bonds between atoms

**Notation**: G = (V, E) where E contains unordered pairs {u, v} indicating an edge between u and v.

---

## Path

A **path** in a graph is a sequence of nodes connected by edges, where you can travel from the first node to the last node by following the edges.

**Characteristics**:
- A path starts at one node and ends at another node
- Each consecutive pair of nodes in the sequence must be connected by an edge
- Nodes in a path (except possibly the first and last) are typically distinct (called a **simple path**)

**In Undirected Graphs**:
- Path: A — B — C — D means you can travel from A to D through B and C
- Example path: [A, B, C, D] represents traveling from A to B to C to D

**In Directed Graphs**:
- Path: A → B → C → D means you can travel from A to D following the direction of arrows
- You must follow the direction of edges
- Example path: [A, B, C, D] only valid if edges are A→B, B→C, C→D

**Types of Paths**:
- **Simple Path**: No node is repeated (except possibly the first and last)
- **Cycle**: A path that starts and ends at the same node
- **Hamiltonian Path**: Visits each node exactly once
- **Eulerian Path**: Uses each edge exactly once

**Path Length**: The number of edges in the path.

---

## Cycle

A **cycle** is a path that starts and ends at the same node, forming a closed loop.

**Characteristics**:
- The first and last nodes are the same
- All other nodes in the cycle are distinct (in a **simple cycle**)
- Contains at least one edge
- In an undirected graph, a cycle must have at least 3 nodes
- In a directed graph, a cycle can have 2 or more nodes

**Undirected Graph Cycles**:
- Example: A — B — C — A forms a cycle (triangle)
- Must have at least 3 nodes and 3 edges

**Directed Graph Cycles**:
- Example: A → B → C → A forms a directed cycle
- Can have 2 nodes: A → B → A (back-and-forth cycle)
- Example: A → B → A (self-cycle with two nodes)

**Types of Cycles**:
- **Simple Cycle**: No repeated nodes except the start/end node
- **Hamiltonian Cycle**: A cycle that visits each node exactly once
- **Eulerian Cycle**: A cycle that uses each edge exactly once

**Acyclic Graphs**:
- A graph with no cycles is called an **acyclic graph**
- An undirected acyclic graph is called a **tree**
- A directed acyclic graph is called a **DAG** (Directed Acyclic Graph)

---

## Degree in Graph

The **degree** of a node is the number of edges connected to that node. However, the definition differs slightly between undirected and directed graphs.

### Degree in Undirected Graph

In an **undirected graph**, the degree of a node is simply the number of edges incident to (connected to) that node.

**Properties**:
- Each edge contributes 2 to the total degree count (one for each endpoint)
- **Handshaking Lemma**: The sum of all degrees in an undirected graph equals 2 × (number of edges)
  - Sum of degrees = 2|E|
- In any graph, the number of nodes with odd degree is always even (or zero)
- Maximum possible degree in a graph with n nodes is n-1 (a node connected to all other nodes)

**Example**:
```
    A — B
    |   |
    C — D
```
- Degree of A = 2 (connected to B and C)
- Degree of B = 2 (connected to A and D)
- Degree of C = 2 (connected to A and D)
- Degree of D = 2 (connected to B and C)
- Sum of degrees = 2 + 2 + 2 + 2 = 8 = 2 × 4 (4 edges)

**Special Cases**:
- **Isolated node**: A node with degree 0 (no connections)
- **Leaf node**: A node with degree 1 (connected to exactly one other node)
- **Regular graph**: A graph where all nodes have the same degree
- **Complete graph**: A graph where every node is connected to every other node (each node has degree n-1)

### Degree in Directed Graph

In a **directed graph**, each node has two types of degrees:

1. **In-degree (indegree)**: The number of edges coming into the node (incoming edges)
2. **Out-degree (outdegree)**: The number of edges going out of the node (outgoing edges)

**Properties**:
- Each directed edge contributes 1 to the total in-degree count and 1 to the total out-degree count
- **Handshaking Lemma for Directed Graphs**: 
  - Sum of all in-degrees = Sum of all out-degrees = Number of edges
  - Sum of all in-degrees = |E|
  - Sum of all out-degrees = |E|

**Example**:
```
    A → B
    ↓   ↑
    C → D
```
- Node A: in-degree = 0, out-degree = 2 (to B and C)
- Node B: in-degree = 1 (from A), out-degree = 1 (to D)
- Node C: in-degree = 1 (from A), out-degree = 1 (to D)
- Node D: in-degree = 2 (from B and C), out-degree = 0
- Sum of in-degrees = 0 + 1 + 1 + 2 = 4 (4 edges)
- Sum of out-degrees = 2 + 1 + 1 + 0 = 4 (4 edges)

**Special Cases**:
- **Source**: A node with in-degree = 0 (no incoming edges)
- **Sink**: A node with out-degree = 0 (no outgoing edges)
- **Isolated node**: A node with both in-degree = 0 and out-degree = 0

**Key Differences**:
- **Undirected**: Single degree value per node
- **Directed**: Two degree values per node (in-degree and out-degree)
- **Undirected**: Degree represents all connections
- **Directed**: In-degree represents dependencies/references, out-degree represents outgoing connections

---

## Edge Weights

**Edge weights** are numerical values assigned to edges in a graph, representing some measure of cost, distance, capacity, strength, or any other quantitative property of the relationship.

**Purpose**:
- Model real-world constraints or properties
- Enable optimization problems (shortest path, minimum spanning tree, etc.)
- Represent distances, costs, capacities, probabilities, etc.

**Types of Weighted Graphs**:

1. **Weighted Undirected Graph**:
   - Edges have weights but no direction
   - Example: Road network where edges represent distances between cities

2. **Weighted Directed Graph**:
   - Edges have both direction and weight
   - Example: Flight routes where edges represent flight duration from one city to another

**Common Applications**:
- **Shortest Path Problems**: Find the path with minimum total weight
- **Minimum Spanning Tree**: Find the tree connecting all nodes with minimum total weight
- **Network Flow**: Edge weights represent capacities
- **Traveling Salesman Problem**: Edge weights represent distances between cities
- **Social Networks**: Edge weights might represent strength of relationships

**Example Weighted Graph**:
```
       5
    A ——— B
    |     |
  3 |     | 2
    |     |
    C ——— D
       4
```
- Edge A-B has weight 5
- Edge A-C has weight 3
- Edge B-D has weight 2
- Edge C-D has weight 4

**Weighted Directed Graph Example**:
```
       5
    A ——→ B
    ↓     ↑
  3 |     | 2
    ↓     ↑
    C ——→ D
       4
```
- Edge A→B has weight 5
- Edge A→C has weight 3
- Edge C→D has weight 4
- Edge D→B has weight 2

**Special Cases**:
- **Unweighted Graph**: All edges have the same weight (often considered weight 1)
- **Negative Weights**: Some applications allow negative edge weights (e.g., profit/loss)
- **Zero Weight**: Edges with weight 0 (free connections)

**Weight Representation**:
- Typically stored as part of the edge data structure
- Can be represented in adjacency matrix as values (instead of 0/1)
- Can be represented in adjacency list as pairs: (destination, weight)

---

## Summary

| Concept | Undirected Graph | Directed Graph |
|---------|------------------|----------------|
| **Edges** | Bidirectional (A—B) | One-directional (A→B) |
| **Degree** | Single value (total connections) | Two values (in-degree, out-degree) |
| **Path** | Can traverse in any direction | Must follow arrow direction |
| **Cycle** | Requires at least 3 nodes | Can have 2+ nodes |
| **Edge Weights** | Applied to bidirectional edges | Applied to directed edges |
| **Handshaking** | Sum of degrees = 2×|E| | Sum of in-degrees = Sum of out-degrees = |E| |

Graphs are fundamental data structures that enable us to model and solve complex problems involving relationships, networks, and dependencies in computer science and real-world applications.

