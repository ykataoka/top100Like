class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.isValid_rows(board)
                and self.isValid_cols(board)
                and self.isValid_3x3(board))

    # time: O(N^2), N = 9
    def isValid_rows(self, board):
        for row in board:
            row = [r for r in row if r != '.']
            if len(set(row)) != len(row):
                return False
        return True

    # time: O(N^2), N = 9
    def isValid_cols(self, board):
        for col in zip(*board):
            col = [c for c in col if c != '.']
            if len(set(col)) != len(col):
                return False
        return True

    # time: O(N^2), N = 9
    def isValid_3x3(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                tmp = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        tmp.append(board[y][x])
                tmp = [t for t in tmp if t != '.']
                if len(set(tmp)) != len(tmp):
                    return False
        return True
