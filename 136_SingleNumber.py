class Solution():
    def SingleNumber(self, nums):
        rest = 0
        for num in nums:
            rest ^= num
        return rest


sol = Solution()
ans = sol.SingleNumber([1,2,3,10,3,2,1,100,10])
print(ans)
