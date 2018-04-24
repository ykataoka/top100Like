class Solution(object):

    # Solution1 : Simply use the set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = set()

        while n not in store:

            # check the ending condition
            if n == 1:
                return True

            # add to store
            store.add(n)

            # convert int -> string
            n_str = str(n)
            n = 0
            for c in n_str:
                n += int(c)**2

        return False

    # Solution2 : fast and slow to remove the 
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = set()

        while n not in store:

            # check the ending condition
            if n == 1:
                return True

            # add to store
            store.add(n)

            # convert int -> string
            n_str = str(n)
            n = 0
            for c in n_str:
                n += int(c)**2

        return False


    def digitSquaredSum(self, n):
        sum = 0
        while n:
            tmp = n % 10
            sum += tmp**2

