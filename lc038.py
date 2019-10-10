# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221


class Solution:
    def countAndSay(self, n: int) -> str:
        def get_next(s: str):
            i = 0
            res = ''
            while i < len(s):
                v = s[i]
                cnt = 1
                j = i+1
                while j < len(s) and v == s[j]:
                    i, j, cnt = i+ 1, j+1, cnt+1
                res = res + (str(cnt) + str(v))
                i += 1
            # print(res)
            return res
        i = 1

        RET = ''
        while i <= n:
            if i == 1:
                RET = '1'
            else:
                RET = get_next(RET)
            i += 1
        return RET


s = Solution()
for i in range(6):
    print(s.countAndSay(i))