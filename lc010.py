# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 示例 3:

# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 示例 4:

# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:

# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not s and p == '.*':
            return True

        d = []
        for i in range(len(p)):

            tmp = []
            for j in range(len(s)):
                if p[i] == '*':
                    tmp.append(-1)
                    break
                elif p[i] == s[j] or p[i] == '.':
                    tmp.append(j)
            d.append(tmp)

        print(d)
        # print(len(s))

        max_repeat = 1
        m = [0] * 26
        for c in s:
            m[ord(c) - ord('a')] += 1
        max_repeat = max(m)
        
        res_ = [False]

        def dfs(i, vals: list, res):
            if res[0]:
                return True

            for t in range(0, len(vals)-1):
                if vals[t+1] - vals[t] != 1:
                    return False

            if i == len(d):
                if len(vals) == len(s):
                    res[0] = True
                    return res[0]

            for j in range(i, len(d)):
                # 如果为空，而且下一个为-1，则跳过
                if not d[j] and j+1 < len(d) and  d[j+1] and d[j+1][0] == -1:
                    continue
                elif d[j] and len(d[j]) == 1 and d[j][0] == -1:  # 如果为-1
                    x = j+1
                    rept = 0
                    while rept < max_repeat:
                        rept += 1
                        for k in d[j-1]:
                            vals.append(k)
                            dfs(x, vals[:], res_)
                            vals.pop()
                else:
                    x = j+1
                    for k in d[j]:
                        vals.append(k)
                        dfs(x, vals[:], res_)
                        vals.pop()
        # d = [[-1], [1, 2], [4, 5, 6]]
        dfs(0, [], res_)
        return res_[0]


s = Solution()
b = s.isMatch('aaa',  "aaaa")
print(b)
# b = s.isMatch('mississippi',  "mis*is*p*.")
# print(b)
# b = s.isMatch('aab', "c*a*b")
# print(b)
"""

