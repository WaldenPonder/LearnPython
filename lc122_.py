# 309
"""
        def get_dp(i):
            if dp[i] != -1:
                return dp[i]
            else:
                for j in range(i):
                    get_dp(j)
                    dp[i] = max(dp[i],  max(dp[0:j-1]) + prices[i] - prices[j])
            return dp[i]
         get_dp(len(prices)-1)
"""

import time


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        max_dp = [0] * len(prices)

        for i in range(1, len(dp)):  # i为卖出
            for k in range(i):  # 买入
                if k <= 1:
                    val = prices[i] - prices[k]
                else:
                    val = max_dp[k-2] + prices[i] - prices[k]
                    # val = max(dp[0: k-1]) + + prices[i] - prices[k]

                dp[i] = max(dp[i], val)
                # print("-- ", i, dp[i])
                if i >= 1:
                    max_dp[i] = max(max_dp[i-1], dp[i])

        return max(dp)


s = Solution()
t = time.clock()

a = [1, 2, 3, 0, 2]

print(s.maxProfit(a))

print("time- ", time.clock() - t)
