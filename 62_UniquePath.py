class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Math: (m+n) C min(m,n) *Comabination Problem
        # DP

        # DP
        hash_map = {(0, 0): 1}
        for x in range(1, m):
            hash_map[(x, 0)] = 1
        for y in range(1, n):
            hash_map[(0, y)] = 1

        for x in range(1, m):
            for y in range(1, n):
                hash_map[(x, y)] = hash_map[(x-1, y)] + hash_map[(x, y-1)]

        return hash_map[(m-1, n-1)]

sol = Solution()
sol.uniquePaths(7, 3)
