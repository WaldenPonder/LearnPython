
null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_tree(l: list):
    root = TreeNode(l[0])
    nodes = [root]

    for i in range(1, len(l)):
        if not l[i]: 
            continue

        newNode = TreeNode(l[i])
        nodes.append(newNode)

        p = nodes[(i-1)//2]
        if i % 2 == 1:
            p.left = newNode
        else:
            p.right = newNode
    return root


def print_tree(t: TreeNode):
    if t is None:
        return
    print(t.val)
    print_tree(t.left)
    print_tree(t.right)


if __name__ == '__main__':
    r = get_tree([3, 9, 20, null, null, 15, 7])
    print_tree(r)