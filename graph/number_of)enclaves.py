class Solution:
    def solve(self, grid) :
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(grid), len(grid[0])
        visited = [[False]* column for _ in range(row)]

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=column or grid[r][c]!=1 or visited[r][c]:
                return
            visited[r][c]=True
            # check in all direction
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # check the row level boundary that is row=0 and row=row-1:
        for c in range(column):
            if grid[0][c] == 1:
                dfs(0,c)
            if grid[row-1][c] == 1:
                dfs(row-1,c)
         
        # check for boundary level column where column=0 and column-1
        for r in range(row):
            if grid[r][0] == 1:
                dfs(r,0)
            if grid[r][column-1] == 1:
                dfs(r, column-1)

        counter = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 and not visited[r][c]:
                    counter+=1
        return counter
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
S = Solution()
print(S.solve(grid))