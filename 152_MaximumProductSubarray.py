class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = nums[0]
        big = nums[0]
        max_sub = nums[0]

        for n in nums[1:]:
            small, big = min(small*n, n, big*n), max(big*n, n, small*n)
            print(small, big)
            max_sub = max(max_sub, big)

        return max_sub
