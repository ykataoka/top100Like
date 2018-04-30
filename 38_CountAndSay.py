class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        Simple coding task
        """
        s = '1'
        for _ in range(n-1):
            out = ''
            cur = s[0]  # current char
            cnt = 0

            for i, char in enumerate(s):
                if char == cur:
                    cnt += 1
                else:
                    out += str(cnt) + cur
                    cur = char
                    cnt = 1
            out += str(cnt) + cur
            s = out
        return s
