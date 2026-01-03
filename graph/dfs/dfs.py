# Create a visited array / set
# Define a recursive DFS function(node)
# Inside DFS(node):
# Mark node as visited
# Process the node (print / store it)
# Loop over each neighbor of node
# If the neighbor is not visited, call DFS(neighbor)
# Call DFS(start_node)

class Solution:
    def dfs(self, adj):
        result = []
        # code here
        visited_array = [False] * len(adj)
        def dfs_internal(node, visited_array):
            for neighbour in adj[node]:
                if not visited_array[neighbour]:
                    visited_array[neighbour] = True
                    result.append(neighbour)
                    dfs_internal(neighbour, visited_array)
        visited_array[0]=True
        result.append(0)
        dfs_internal(0, visited_array)
        return result
    

adj =[[2, 3, 1], [0], [0, 4], [0], [2]]
S = Solution()
print(S.dfs(adj))





