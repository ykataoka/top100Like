class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix "in-place" instead.
        """
#        A[:] = zip(*A[::-1])
#        A[:] = zip(*A[::-1])
#        tmp = [list(vec)[::-1] for vec in zip(*matrix)]
        A[:] = [list(vec)[::-1] for vec in zip(*A)]
#        matrix = tmp
#        print(matrix)
