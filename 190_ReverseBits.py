class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        for i in range(31, -1, -1):
            if n % 2 == 1:
                out += pow(2, i)
            n = int(n/2)
        return out
