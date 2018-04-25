class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board[0])  # X
        m = len(board)     # Y
        for x in range(n):
            for y in range(m):
                cnt = self.count_live(board, x, y)
                print(cnt)
                if board[y][x] % 2 == 0:
                    if cnt == 3:
                        board[y][x] = 2
                else:
                    if cnt < 2 or 3 < cnt:
                        board[y][x] = 3

        for x in range(n):
            for y in range(m):
                if board[y][x] == 3:
                    board[y][x] = 0
                elif board[y][x] == 2:
                    board[y][x] = 1

    def count_live(self, board, x, y):
        n = len(board[0])  # X
        m = len(board)     # Y
        cnt = 0
        if (x-1 >= 0) and (y-1 >= 0):
            cnt += board[y-1][x-1] % 2
        if (y-1 >= 0):
            cnt += board[y-1][x] % 2
        if (x+1 < n and y-1 >= 0):
            cnt += board[y-1][x+1] % 2

        if (x-1 >= 0):
            cnt += board[y][x-1] % 2
        if (x+1 < n):
            cnt += board[y][x+1] % 2

        if (x-1 >= 0) and (y+1 < m):
            cnt += board[y+1][x-1] % 2
        if (y+1 < m):
            cnt += board[y+1][x] % 2
        if (x+1 < n and y+1 < m):
            cnt += board[y+1][x+1] % 2
        return cnt
