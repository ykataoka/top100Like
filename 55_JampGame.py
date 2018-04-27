class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0  # the max index that can be reached
        for i, s in enumerate(nums):
            if i > m:  # if the index is not reachable, return False
                return False
            m = max(m, i+s)
            if m > len(nums):
                return True
        return True
   
