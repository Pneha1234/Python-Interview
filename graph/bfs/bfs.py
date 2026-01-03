# Create a queue

# Create a visited set / array

# Put the starting node into the queue

# Mark the starting node as visited

# While the queue is not empty:

    # Pop (dequeue) a node from the queue

    # For each neighbor of that node:

    # If the neighbor is not visited:

    # Mark it as visited

    # Add (enqueue) it to the queue


from collections import deque
class Solution:
    def bfs(self, adj):
        queue = deque()
        visited_array = [False]*len(adj)
        queue.append(0)
        visited_array[0]=True
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbour in adj[node]:
                if not visited_array[neighbour]:
                    visited_array[neighbour]= True
                    queue.append(neighbour)


adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

s =Solution()
s.bfs(adj)

