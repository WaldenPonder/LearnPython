class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        ret = 0
        i = 0
        while i < len(prices):
            low = prices[i]
            x = i
            for j in range(x, len(prices)):  # 找到low                
                if low < prices[j]:
                    break
                else:
                    low = prices[j]
                    i = j

            hi = prices[j]
            x = j
            for k in range(x, len(prices)):
                if hi > prices[k]:
                    break
                else:
                    hi = prices[k]
                    i = k
            i += 1
            ret += hi - low
        return ret


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
