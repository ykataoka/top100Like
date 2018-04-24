class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        # main case
        max_profits = [None] * len(nums)
        max_profits[0] = nums[0]
        max_profits[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_profits[i] = max(max_profits[i-1], max_profits[i-2] + nums[i])
        return max(max_profits[-1], max_profits[-2])
