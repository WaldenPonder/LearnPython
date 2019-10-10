
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next and id(cur) < id(cur.next):
                return cur.next
            cur = cur.next

        return None


for i in [1, 2, 3, 4, 5]:
    print(id(i))
