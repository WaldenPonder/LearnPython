# class Solution:
#     def generateTrees(self, n: int):
#         dp = [0] * (n+1)
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 5

#         for i in range(2, len(dp)):
#             dp[i] = 2 * dp[i-1] + i-1
#         print(dp)
#         return dp[-1]


# s = Solution()
# b = s.generateTrees(4)
# print(b)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n < 1:
            return res
        else:
            return self.generateBST(1, n) 
        
    def generateBST(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        else:
            for i in range(start, end + 1):
                # 左子树
                left_tree = self.generateBST(start, i - 1)
                # 右子树
                right_tree = self.generateBST(i + 1, end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        print('root  ', root.val)
                        res.append(root)
            # print(res)
            return res


s = Solution()
v = s.generateTrees(3)
# print(v)
