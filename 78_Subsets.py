class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Solution1 : bfs
        res = []
        self.bfs(nums, [], 0, res)
        return res

    def bfs(self, nums, path, index, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.bfs(path, nums+[nums[i]], i+1, res)
