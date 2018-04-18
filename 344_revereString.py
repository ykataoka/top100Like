import doctest

class Solution(object):

    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str

        Recursive Approach

        >>> test.reverseString1('hoge')
        'egoh'

        >>> test.reverseString1('')
        ''

        >>> test.reverseString1('abcdefg1234567890')
        '0987654321gfedcba'

        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s[0]
        return s[-1] + self.reverseString1(s[:-1])

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str

        Pythonic Approach

        >>> test.reverseString2('hoge')
        'egoh'

        >>> test.reverseString2('')
        ''

        >>> test.reverseString2('abcdefg1234567890')
        '0987654321gfedcba'

        """
        return s[::-1]
    
test = Solution()
result = test.reverseString1('abcdefg')
print(result)

doctest.testmod(extraglobs={'test': Solution()})
