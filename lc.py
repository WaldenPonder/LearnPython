from create_tree_from_list import null
from create_tree_from_list import TreeNode
import create_tree_from_list as ct


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        def get_min(root, k):
            stk = [root]
            while stk:
                r = stk.pop()
                if r.val != k:
                    return r.val
                if r.left:
                    stk.append(r.left)
                if r.right:
                    stk.append(r.right)

        vec = [root.val]
        if root.left:
            vec.append(root.left.val)
        if root.right:
            vec.append(root.right.val)

        if len(vec) == 1:
            return -1

        if len(vec) == len(set(vec)):
            return min(vec[1], vec[2])

        res = []
        if root.left:
            v = get_min(root.left, root.val)
            if v:
                res.append(v)
        if root.right:
            v = get_min(root.right, root.val)
            if v:
                res.append(v)
        if res:
            return min(res)
        else:
            return -1


r = ct.get_tree([2, 3, 2])
s = Solution()
b = s.findSecondMinimumValue(r)
print(b)
