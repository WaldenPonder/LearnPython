# Definition for singly-linked list.
from create_list_node_from_list import ListNode, print_list, get_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur = head
        pre = head

        while cur:
            tmp = cur.next
            while tmp and tmp.val == cur.val:
                tmp = tmp.next
            cur = tmp
            pre.next, pre = cur, cur
        return head


s = Solution()
print_list(s.deleteDuplicates(get_list([1, 1,  2, 3, 3, 4, 5, 5])))
