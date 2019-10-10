
class Solution:

    def part(self, prices) -> int:
        if not prices:
            return 0
        minValue = prices[0]
        ret = 0

        for i in range(1, len(prices)):
            if prices[i] - minValue > ret:
                ret = prices[i] - minValue
            if prices[i] < minValue:
                minValue = prices[i]
        return ret

    def maxProfit(self, prices) -> int:
        if len(prices) == 2:
            t = prices[1] - prices[0]
            return t if t > 0 else 0
        elif len(prices) == 3:
            return max(0, prices[2] - prices[0], prices[1] - prices[0], prices[2] - prices[1])

        ret = 0
        for i in range(2, len(prices)-1):
            tmp = self.part(prices[:i+1]) + self.part(prices[i:])

            ret = max(tmp, ret)
        return ret