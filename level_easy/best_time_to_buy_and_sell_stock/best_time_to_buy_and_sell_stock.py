class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for actual_price in prices :
            if actual_price < min_price :
                min_price = actual_price
            else :
                max_profit = max(max_profit, actual_price - min_price)

        return max_profit
