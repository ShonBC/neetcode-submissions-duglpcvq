class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        ans = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                ans = max(profit, ans)
            else:
                buy = sell
            sell += 1
        return ans
            