class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if nums == []:
            return 0

        # Solution1 : DP
        # T: store the lengthOfLIS UP TO each index
        T = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    T[i] = max(T[i], T[j]+1)
        return max(T)
