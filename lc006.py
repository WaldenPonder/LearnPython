class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []

        i = 0
        d = 0

        while i < len(s):
            r = ['*'] * numRows
            res.append(r)
            d -= 1
            if d <= 0:
                d = numRows - 1

            if d == numRows - 1:
                tmp = 0
                while i < len(s) and tmp <= d:
                    r[tmp] = s[i]
                    tmp += 1
                    i += 1
            else:
                r[d] = s[i]
                i += 1

        ret = []
        for j in range(numRows):
            for i in range(len(res)):
                if res[i][j] != '*':
                    ret.append(res[i][j])

        return ''.join(ret)


s = Solution()
v = s.convert('LEETCODEISHIRING', 4)
print(v)
