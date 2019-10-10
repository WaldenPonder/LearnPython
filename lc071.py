class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst = []
        for c in path.split('/'):
            if c:
                lst.append(c)

        res = []
        for c in lst:
            if c == '.':
                continue
            elif c == '..':
                if res:
                    res.pop()
            else:
                res.append(c)
                
        if not res:
            return '/'
        res.insert(0, '')
        return '/'.join(res)


s = Solution()
# v = s.simplifyPath("/a/../../b/../c//.//")
# print(v)
# v = s.simplifyPath("/a//b////c/d//././/..")
# print(v)
# v = s.simplifyPath("/a/./b/../../c/")
# print(v)
v = s.simplifyPath("/../")
print(v)
v = s.simplifyPath("/home//foo/")
print(v)