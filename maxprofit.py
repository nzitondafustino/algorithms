class Solution:
    def maxProfit(self, prices) -> int:

        if len(prices) < 2:
            return 0
        current_buy, current_sell = 0,1
        next_buy = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[current_buy] and prices[i] < prices[next_buy]:
                next_buy = i
            if prices[i] - prices[current_buy] > prices[current_sell] - prices[current_buy]:
                current_sell = i
            if prices[current_sell] - prices[current_buy] < prices[i] - prices[next_buy]:
                current_buy = next_buy
                current_sell = i
        profit = prices[current_sell] - prices[current_buy]
        return profit if profit > 0 else 0



class Solution:
    def maxProfit(self, prices) -> int:
        L,R = 0,1
        maxProfit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                maxProfit = max(maxProfit, prices[R] - prices[L])
            else:
                L = R 
            R +=1

        return maxProfit