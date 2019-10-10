class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0

        firstChar = str[0]
        start = 0
        fh = 1
        if firstChar == '+':
            start = 1
        elif firstChar == '-':
            start = 1
            fh = -1
        res = 0
        for i in range(start, len(str)):
            if ord('0') <= ord(str[i]) <= ord('9'):
                res = res * 10 + ord(str[i]) - ord('0')
            else:
                break

        if -2 ** 31 <= fh * res <= 2 ** 31 - 1:
            return fh * res
        elif fh * res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif fh * res < -2 ** 31:
            return -2 ** 31


s = '  aa '
print(s)
print(s.strip())