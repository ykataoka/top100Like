class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1: Hashmap -> Obvious, Time: O(N), Space: O(N)
        # Solution 2: Sort -> Obvious, Time: O(N log(N)), Space: O(1)
        # Solution 3: use 'counter', Time: O(N), Space: O(1)!!

        # Solution 3
        cnt = 0
        max_num = nums[0]
        for num in nums:
            if cnt > 0:
                if max_num == num:
                    cnt += 1
                else:
                    cnt -= 1
            else:
                max_num = num
                cnt += 1

        return max_num


s = Solution()
print(s.majorityElement([4, 3, 2, 2, 2, 2, 3, 1, 2]))
print(s.majorityElement([6, 5, 5]))
print(s.majorityElement([3, 3, 4]))
