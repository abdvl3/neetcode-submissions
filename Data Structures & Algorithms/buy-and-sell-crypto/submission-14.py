class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #loop through each price, if price on the right lower, new low and continue
        l = 0
        maxP = 0

        for r in range (len(prices)):
            if prices[r] < prices[l]:
                l = r
            
            maxP = max(maxP,prices[r]-prices[l])
        
        return maxP
