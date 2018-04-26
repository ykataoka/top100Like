class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Base case
        if len(s) == 0:
            return True

        for i in range(len(s)):
            if s[0:i+1] in wordDict:
                if self.wordBreak(s[i+1:], wordDict):
                    return True
        return False
