class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        N = len(nums)
        k = k % N

        # Solution 1: Pythonic way
        # nums[:] = nums[-k:] + nums[:(N-k)]

        # Solution 2: 12345, k=2, 321+54 -> 45123
        print(N, k)
        print(self.swap_arr(nums[-k:]))
        print(self.swap_arr(nums[:(N-k)]))
        nums[:] = self.swap_arr(self.swap_arr(nums[:(N-k)]) + self.swap_arr(nums[-k:]))

    def swap_arr(self, nums):
        print(nums)
        if len(nums) >= 2:
            for i in range(0, len(nums)/2):
                nums[i], nums[-(i+1)] = nums[-(i+1)], nums[i]
        return nums
