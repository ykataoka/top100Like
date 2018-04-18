class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1 convert the num of index to positive
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = - abs(nums[idx])

        # 2 extract the positive number's index
        out = []
        for i, num in enumerate(nums):
            if num > 0:
                out.append(i+1)
        return out


hoge = Solution()
print(hoge.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
