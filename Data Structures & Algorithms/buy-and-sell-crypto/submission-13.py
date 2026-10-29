class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r = 0,1
        maxP = 0

        # want day that has the lowest price + day after with highest price

        while r < len(prices):

            if prices[r] < prices[l] and r < len(prices) - 1:
                l = r
                r += 1

            maxP = max(maxP, prices[r] - prices[l])
            
            r += 1
        
        return maxP
        