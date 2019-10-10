class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        jinwei = 0
        lst = []
        while i >= 0 or j >= 0:
            s = jinwei
            if i >= 0:
                s += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(b[j]) - ord('0')
                j -= 1
            lst.append('1' if (s % 2) == 1 else '0')
            jinwei = s // 2
        if jinwei:
            lst.append('1')
        lst = lst[::-1]
        return ''.join(lst)


# "11101"
# 预期结果
# "10101"
# 1010
# 1011
s = Solution()
print(s.addBinary(a="1010", b="1011"))
