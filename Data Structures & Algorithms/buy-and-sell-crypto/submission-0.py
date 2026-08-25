class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest buying price
        max_profit = 0            # Track the peak profit

        for price in prices:
            # Update min_price if a cheaper buy day is found
            if price < min_price:
                min_price = price
            # Calculate profit if sold today, update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit      