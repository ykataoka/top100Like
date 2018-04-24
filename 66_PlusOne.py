class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # convert to number
        tens = len(digits)
        ans = 0
        for i, digit in enumerate(digits):
            ans += digit * pow(10, tens-(i+1))
            print(ans)
        # convert to array
        return [int(d) for d in list(str(ans+1))]
