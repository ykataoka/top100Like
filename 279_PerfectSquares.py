import math

class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # create the list of the squared number
        max_base = int(math.pow(n, 1/2.))
        cands = [pow(i, 2) for i in range(1, max_base+1)]

        # run the bfs
        cnt = 0
        to_check = set([n])  # queue for each level
        while to_check:  #
            cnt += 1
            tmp = set()
            for target in to_check:
                for cand in cands:
                    if target == cand:
                        return cnt
                    if target < cand:
                        break
                    tmp.add(target - cand)
            to_check = tmp

        return cnt
