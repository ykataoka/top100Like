class Solution(object):

#    # Solution1 : Simply use the set()
#    def isHappy(self, n):
#        """
#        :type n: int
#        :rtype: bool
#        """
#        store = set()
#
#        while n not in store:
#
#            # check the ending condition
#            if n == 1:
#                return True
#
#            # add to store
#            store.add(n)
#
#            # convert int -> string
#            n_str = str(n)
#            n = 0
#            for c in n_str:
#                n += int(c)**2
#
#        return False

    # Solution2 : fast and slow to avoid the extra space
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while fast != 1 and slow != 1:

            # compute slow
            slow = self.digitSquaredSum(slow)
            
            # compute fast
            fast = self.digitSquaredSum(fast)
            fast = self.digitSquaredSum(fast)
            print('slow, fast:', slow, fast)
            # check the cycle condition
            if (slow != 1) and (slow == fast):
                return False

        return True


    def digitSquaredSum(self, n):
        sum_ = 0
        while n:
            tmp = n % 10
            sum_ += tmp**2
            n = n / 10
        return sum_
