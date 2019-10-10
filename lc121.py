class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        minValue = prices[0]
        ret = 0

        for i in range(1, len(prices)):
            if prices[i] - minValue > ret:
                ret = prices[i] - minValue
            minValue = min(minValue, prices[i])
        return ret


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
