class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) - Sliding Window solution - Cleaner than last submission
        
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1

        return maxProfit

