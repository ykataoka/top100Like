class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        key 1: Use quick-select. This will be O(n) in average.
        Like quick sort, partioning algorithm is used.
        The difference is one partition can be neglected for sorting.
        """
        n = len(nums)
        pivot = n/2
        left, right = [], []

        # base case
        if n == 1:
            return nums[0]

        # divide into two partition
        for num in nums:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)

        # recursive

        # if the k is in the right
        if len(left) > k:
            return self.findKthLargest(right, k-len(left))
        # if the k is in the left
        elif len(left) <= k:
            return self.findKthLargest(left, k)


        # Solution 2: sort O(n logn)
        return sorted(nums, reverse=True)[k-1]
