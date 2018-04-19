class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1 : O(N) time and O(N) memory
        max_till_i = [None]*len(nums)  # O(N) space complexity
        tmp = 0

        for i, num in enumerate(nums):
            # add the current number and save it to max_till_i
            tmp = tmp + num
            max_till_i[i] = tmp

            # if tmp is negative, there is no reason to add the past sub array from i
            # Thus, initialize to 0
            if tmp < 0:
                tmp = 0

        # return the max value of max_till_i
        return max(max_till_i)

    # Solution 2 : O(N) time and O(1) memory!
    #    def maxSubArray(self, nums):
    #        """
    #        :type nums: List[int]
    #        :rtype: int
    #        """
    #        if not nums:
    #            return 0
    #
    #        curSum = maxSum = nums[0]
    #        for num in nums[1:]:
    #            curSum = max(num, curSum + num)  # if adding past data does not increase the value, then consider the sum to current position as num solely
    #            maxSum = max(maxSum, curSum)
    #
    #        return maxSum
