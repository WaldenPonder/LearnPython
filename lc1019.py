from create_list_node_from_list import ListNode, print_list, get_list
from typing import List
import heapq as hq


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next

        LEN = len(lst)
        i = LEN - 1

        dp = [0] * LEN
        while i >= 0:
            if i >= LEN - 1:
                i -= 1
                continue
            j = i
            while j < LEN:
                if lst[i] < lst[j]:
                    dp[i] = lst[j]
                    break
                elif lst[i] < dp[j]:
                    dp[i] = dp[j]
                    break
                elif j != i and dp[j] == 0:
                    break
                j += 1
            i -= 1
        
        i, cur = 0, head
        while cur:
            cur.val = dp[i]
            cur = cur.next
            i += 1

        return head          


s = Solution()
print_list(s.nextLargerNodes(get_list([2, 7, 4, 3, 5])))
print_list(s.nextLargerNodes(get_list([1, 7, 5, 1, 9, 2, 5, 1])))

# h = []
# for i in [1, 2, 3, 3, 2, 1]:
#     hq.heappush(h, i)

# print(h)


# lst = []
# while h:
#     lst.append(hq.heappop(h))
# print(lst)


# h = [1, 2, 3, 4, 4, 3, 2, 1]
# hq.heapify(h)
# print(hq.nlargest(len(h), h))