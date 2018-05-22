class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # Solution 1 : Naive Approach
        # out = 0
        # for i in range(31, -1, -1):
        #     if n % 2 == 1:
        #         out += pow(2, i)
        #         n = int(n/2)
        # return out

        # Solution 2 : Simple Bit Manipulation (should faster than pow)
        # out = 0
        # for _ in xrange(32):
        #     out = out << 1
        #     out += (n & 1)  # take out the most right digit
        #     n = n >> 1
        # return out

        # Solution 3 : O(1) bit manipulation
        n_max = pow(2, 32) - 1  # regular unsigned int max
        n = (n << 16 | n >> 16) & n_max
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1
        return n
