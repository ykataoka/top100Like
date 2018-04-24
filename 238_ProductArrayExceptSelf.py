class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        out = [1]*len(nums)

        # forward
        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i-1]
            out[i] = out[i] * tmp

        # backward
        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1]
            out[i] = out[i] * tmp

        return out
