from typing import List

def maxProfit(prices: List[int]) -> int:
    # O(n^2): brute force
    # profit = 0
    # for index, x in enumerate(prices[:-1]): # price you buy : skip last element
    #     for y in prices[index:]: # price you sell : start after element x
    #         if (y - x) > profit:
    #             profit = y - x
    
    # O(n): looping through once while tracking max profit and min price
    min_price, max_profit = prices[0], 0
    for x in prices:
        max_profit = max(max_profit, x - min_price)
        min_price = min(min_price, x)
    return max_profit

prices = [7,1,5,3,6,4]
# output = 5
print(maxProfit(prices))

prices = [7,6,4,3,1]
# output = 0
print(maxProfit(prices))