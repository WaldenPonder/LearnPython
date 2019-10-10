import copy
import sys

class Solution:
    def minimumTotal(self, tri) -> int:
        dp = copy.deepcopy(tri)
        dp[0][0] = tri[0][0]

        for i in range(1, len(tri)):
            for j in range(len(tri[i])):
                if j == 0:
                    dp[i][j] = tri[i][j] + dp[i-1][j]
                elif j == len(tri[i])-1:
                    dp[i][j] = tri[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = tri[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        print(dp)
        return min(dp[-1])


print(sys.path)