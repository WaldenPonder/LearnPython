from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = set()

        for i in range(len(nums)):
            c = 0 - nums[i]
            if c in d:
                return [d[c], nums[i]]
            d.add(nums[i])
        

s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
