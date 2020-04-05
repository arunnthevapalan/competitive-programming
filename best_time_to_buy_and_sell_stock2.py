'''
Problem 05 - 05/04/2020
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        i=1
        max_profit = 0
        while(i<len(prices)):
            if prices[i]>prices[i-1]:
                max_profit += prices[i]-prices[i-1]
            i+=1
        return max_profit
            
            
        
            
            
        
