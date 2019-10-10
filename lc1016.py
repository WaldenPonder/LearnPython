class Solution:
    def queryString(self, S: str, N: int) -> bool:
        def to_string(N):
            lst = []
            while N:
                lst.insert(0, chr(N % 2 + ord('0')))
                N //= 2
            return ''.join(lst)

        i = 1
        while i <= N:
            if to_string(5) not in S:
                return False
            i += 1
        return True


s = Solution()
b = s.queryString("10010111100001110010", 10)
print(b)
