class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(n)
        if n < 0:
            n = -n
            x = 1./x
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x

        # even number
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n/2), 2)
        if n % 2 == 1:
            return 1./x*self.myPow(self.myPow(x, (n+1)/2), 2)
            
