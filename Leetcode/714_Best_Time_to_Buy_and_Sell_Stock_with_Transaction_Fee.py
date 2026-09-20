class Solution:
    def maxProfit(self, prices, fee):
        cash=0; hold=-prices[0]
        for p in prices[1:]:
            old_cash=cash
            cash=max(cash,hold+p-fee)
            hold=max(hold,old_cash-p)
        return cash