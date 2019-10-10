class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i-1] == '(':  # 前一个为（
                    dp[i] = 2
                    if i - 2 >= 0:
                        dp[i] += dp[i-2]
                else:  # 前一个为)
                    index = i - dp[i-1] - 1
                    if index >= 0:
                        dp[i] = dp[i-1]+2 if s[index] == '(' else 0
                        if index >= 1:
                            dp[i] += dp[index-1]
        print(dp)
        return max(dp)

# "(( )) ) () )("
s = Solution()
s.longestValidParentheses("(()))())(")

