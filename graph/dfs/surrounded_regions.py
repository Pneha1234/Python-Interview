class Solution:
    def solve(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        visited = [[False]* column for _ in range(row)]

        def dfs(r,c):
            if 0<=r<row or 0<=c<column or board[r][c]!=0 or visited[r][c]:
                return
            visited[r][c]=True
            # check in all direction
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # check the row level boundary that is row=0 and row=row-1:
        for c in range(column):
            if board[0][c] == 0:
                dfs(0,c)
            if board[row-1][c] == 0:
                dfs(row-1,c)
         
        # check for boundary level column where column=0 and column-1
        for r in range(row):
            if board[r][0] == 0:
                dfs(r,0)
            if board[r][column-1] == 0:
                dfs(r, column-1)

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'O' and not visited[r][c]:
                    board[r][c] = 'X'
board =[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
S = Solution()
print(S.solve(board))