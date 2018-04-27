class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out = []
        while matrix != []:
            tmp = matrix.pop(0)
            out = out + tmp
            matrix = [list(m) for m in zip(*matrix)][::-1]
            print(matrix)
        return out
