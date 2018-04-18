class Solution(object):
    def hammingDistance(self, x, y):
        xor = x^y  # exclusive or
        c = 0  # counter

        while xor:
            if xor & 1 == 1:
                c += 1
            xor = xor >> 1

        return c


print(bin(100))
print(bin(200))
print(bin(100^200))
    
sol = Solution()
ans = sol.hammingDistance(100, 200)
print(ans)
