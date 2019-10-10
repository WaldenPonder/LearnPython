# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []

        stk = []
        res = []

        cur = root
        while stk or cur:

            while cur:
                stk.append(cur)
                cur = cur.left

            cur = stk.pop()
            cur = cur.right
            while cur:
                stk.append(cur)
                cur = cur.right
             
            cur = stk.pop()
            stk.pop()
            res.append(cur.val)
            cur = None
        return res


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

"""
    2
  3    4
1   5


f(r)
{
    f(r.l)
    f(r.r)
    print(r)
}
"""
t2.left = t3
t2.right = t4
t3.left = t1
t3.right = t5

s = Solution()
print(s.inorderTraversal(t2))
