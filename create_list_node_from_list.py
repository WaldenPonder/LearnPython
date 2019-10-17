class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_list(vals):
    lst = ListNode(vals[0])
    head = lst
    for i in range(1, len(vals)):
        newList = ListNode(vals[i])
        lst.next = newList
        lst = newList
    return head


def print_list(lst):
    LST = []
    while lst:
        LST.append(lst.val)
        lst = lst.next
    print(LST)
