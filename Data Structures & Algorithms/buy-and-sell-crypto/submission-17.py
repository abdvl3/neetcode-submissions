class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #find the lowest buying point, and the highest selling point after

        buy = 0
        maxP = 0

        for sell in range(len(prices)):
            
            if prices[sell] < prices[buy]:
                buy = sell

            maxP = max(maxP,prices[sell] - prices[buy])
        
        return maxP