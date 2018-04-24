class Solution(object):
    ans = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        candidates = sorted(candidates)
        path = []
        self.dfs(candidates, target, 0, path)
        return self.ans

    def dfs(self, nums, target, idx, path):
        if target < 0:
            return
        if target == 0:
            self.ans.append(path)
            return
        if target > 0:
            for i in range(idx, len(nums)):
                self.dfs(nums, target-nums[i], i, path + [nums[i]])
