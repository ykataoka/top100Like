class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.arrayTrees([i+1 for i in range(n)])
        
    def arrayTrees(self, arr):
        # base case
        if len(arr) == 1:
            return 1

        # recursive
        ans = 0
        for i, a in enumerate(arr):
            ans += self.arrayTrees([arr[:i] + arr[i+1:]])

        return ans
