# Convert adjacency matrix to adjacency list
# Create a visited array initialized to False
# Initialize province_count = 0
# Loop over all nodes:
    # If the node is not visited:
        # Run DFS from that node
        # Increment province_count
# Return province_count

#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        visited = [False] * V
        province_count = 0

        def dfs(node):
            visited[node] = True
            for neighbour in range(V):
                if adj[node][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        for i in range(V):
            if not visited[i]:
                province_count += 1
                dfs(i)

        return province_count



