class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Naive Solution
        # O(n^2)

        max = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    if (profit > max):
                        max = profit
        return max
        
