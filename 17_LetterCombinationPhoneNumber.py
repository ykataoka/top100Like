class Solution(object):
    phone_num2str = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # base case : if digit is the last digit
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return self.phone_num2str[digits]

        # recursive
        former, latter = digits[0], digits[1:]
        out = []
        for add_str in self.phone_num2str[former]:
            for perm in self.letterCombinations(latter):
                out.append(add_str + perm)

        return out
