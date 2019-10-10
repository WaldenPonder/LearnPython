from typing import List
import time

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)
        k_ = 0
        for i in range(len(A)):
            cnt = 0
            
            if A[i] == 1 or k_ > 0:
                cnt = dp[i-1] + 1
                if A[i] == 0:
                    k_ -= 1
            else:
                k_ = K
                j = i
                while j >= 0 and k_ >= 0:                
                    if A[j] == 0:
                        k_ -= 1
                    if k_ >= 0 or A[j] == 1:
                        cnt += 1
                    j -= 1
            dp[i] = cnt
            i += 1
        return max(dp)


s = Solution()
i = 0
t = time.clock()
while i < 10000:
    b = s.longestOnes(A=[0, 0, 1, 1, 0,
                         0, 1, 1, 1, 0,
                        1, 1, 0, 0, 0, 
                        1, 1, 1, 1], K=3)
    i += 1

print(b, time.clock() - t)
