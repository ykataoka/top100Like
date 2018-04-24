# Solution 1: save the current min value as the tuple

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # [(num, min_val upto here)]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # update the min value
        if self.stack == []:
            self.stack.append((x, x))  # x can be the min number
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack == []:
            raise 'error: length is wrong'
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
