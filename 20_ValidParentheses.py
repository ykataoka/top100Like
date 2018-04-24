class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        checker = {')': '(', '}': '{', ']': '['}

        for b in s:  # b refers to single bracket
            if stack != []:
                # closing bracket case
                if b in checker:
                    if stack[-1] == checker[b]:
                        stack.pop()
                    else:
                        stack.append(b)
                # open bracket
                else:
                    stack.append(b)
            else:
                stack.append(b)
        return stack == []


sol = Solution()
print(sol.isValid([']']))
