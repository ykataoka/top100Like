class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        future_max_values = [None]*len(prices)
        max_profits = [None]*len(prices)
        max_tmp = 0
        for i in [len(prices) - j-1 for j in range(len(prices))]:
            max_tmp = max(max_tmp, prices[i])
            future_max_values[i] = max_tmp
        # print(future_max_values)
        
        # 2. make the potential max profit list
        for i, price in enumerate(prices):
            max_profits[i] = future_max_values[i] - prices[i]
        
        return max(max_profits)
