import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
        key 1: use heap data structure to easily takeout the min numbers.
        https://www.cs.cmu.edu/~adamchik/15-121/lectures/Binary%20Heaps/heaps.html
        """

        # count the number of occurence
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        # create the (occurence, number) list
        freq_nums = []
        for val, occur in counter.items():
            heapq.heappush(freq_nums, (-occur, val))  # min order

        # return the values
        k_vals = []
        for i in range(k):
            k_vals.append(heapq.heappop(freq_nums)[1])
        return k_vals
