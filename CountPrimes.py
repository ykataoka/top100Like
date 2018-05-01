import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        input 2; 0 ()
        input 3; 1 (2)
        input 4; 2 (2,3)
        input 5; 2 (2,3)
        input 6; 3 (2,3,5)
        input 10; 4 (2,3,5,7)
        """
        if n < 3:
            return 0

        # Solution1 : naive solution (Time exceeds)
        # prime = [False, False, True, ...] (0,1,2,...,n-1)
        # key 1 : check the prime up to int(sqrt(k))
        # case 29) sqrt(29) = 5.*** check the divisor up to 5
        primes = [False, False, True] + [True]*(n-3)
        for k in xrange(2, n):
            for i in xrange(2, int(math.sqrt(k))+1):
                if float(k) / i == float(k) // i:
                    primes[k] = False
                    break
        return sum(primes)

        # Solution2 : delete the number by the the prime number incrementally
        # prime = [False, False, True, ...] (0,1,2,...,n-1)
        # key 1 : check the prime up to int(sqrt(k))
        # note 1 : A[0:10:2] = ['hoge']*len(A[0:10:2]), change just odd numbers
        primes = [False, False, True] + [True]*(n-3)
        for k in xrange(2, n):
            if primes[k]:
                primes[k:n:k] = [False]*len(primes[k:n:k])
                primes[k] = True  # change
        return sum(primes)
