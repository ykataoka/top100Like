class Solution(object):

    # Solution 1: DP
#    def permute(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
#        # base case
#        if nums == []:
#            return
#        
#        # recursive
#        ans = []
#        for i, num in enumerate(nums):
#            tmp = []
#            tmp.append(num)
#            tmp = tmp + self.permute(nums[:i]+nums[i+1:])
#            ans.append(tmp)
#        return ans

    # Solution 2: DFS
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        # base case: end condition
        if nums == []:
            res.append(path)
            return

        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
