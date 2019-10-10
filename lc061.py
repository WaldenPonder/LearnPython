
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        if k == 0 or not head.next:
            return head

        cnt = 0
        cur = head
        while cur and cur.next:
            cnt += 1
            cur = cur.next
        cnt += 1
        cur.next = head

        i = 1
        cur = head
        while i < cnt - k % cnt:
            i += 1
            cur = cur.next
        pre = cur.next
        cur.next = None
        return pre


def creat_list_node(lst):
    n = ListNode(lst[0])
    h = n
    for i in range(1, len(lst)):
        v = ListNode(lst[i])
        n.next = v
        n = v
    return h


s = Solution()

res = s.rotateRight(creat_list_node([1, 2, 3]), 2)

while(res):
    print(res.val)
    res = res.next
