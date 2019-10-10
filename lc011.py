
class Solution:
    def maxArea(self, height) -> int:
        lo = 0
        hi = len(height) - 1
        res = 0
        while lo < hi:
            res = max(res, min(height[lo], height[hi]) * (hi - lo))

            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return res


s = Solution()
r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)
