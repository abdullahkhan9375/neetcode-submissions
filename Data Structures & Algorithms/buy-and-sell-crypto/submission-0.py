class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx1 = 0
        idx2 = 1
        prev = 0
        while (idx1 < len(prices) - 1):
            buy = prices[idx1]
            sell = prices[idx2]
            print(buy, sell)
            prof = sell - buy
            if (prof > prev):
                prev = prof
            
            idx2 += 1
            if (idx2 > len(prices) - 1):
                idx1 += 1
                idx2 = idx1 + 1
        return prev
