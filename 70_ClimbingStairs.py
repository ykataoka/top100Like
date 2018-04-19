class Solution(object):
    def climbStairs(self, n):
        num_table = {1:1, 2:2}  # fill out the obvious solution
        if n < 3:
            return num_table[n]
        else:
            for i in range(3, n+1):
                num_table[i] = num_table[i-1] + num_table[i-2]
        return num_table[n]
