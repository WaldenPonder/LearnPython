class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        lst = list(strs[0])

        for i in range(1, len(strs)):
            for j in range(max(len(strs[i]), len(lst))):
                if j >= len(lst) or j >= len(lst) or j >= len(strs[i]) or lst[j] != strs[i][j]:
                    lst = lst[:j]
                    break
        return ''.join(lst)


s = Solution()
b = s.longestCommonPrefix(["aab", "aac"])
print(b)
