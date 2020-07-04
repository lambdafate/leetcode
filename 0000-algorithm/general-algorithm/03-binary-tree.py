"""
    反转二叉树
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
def solution(root):
    if root is None:
        return None
    root.left, root.right = solution(root.right), solution(root.left)
    return root

# 迭代


def solution1(root):
    if root is None:
        return None
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        nodes.append(node.left)
        nodes.append(node.right)
    return root


def test(root1, root2):
    assert (root1 == root2) or root1.val == root2.val
    if root1 and root2:
        test(root1.left, root2.left)
        test(root1.right, root2.right)


def cat(root):
    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        if node:
            print(f"{node.val} => ", end="")
            nodes.append(node.left)
            nodes.append(node.right)
    print("None")


if __name__ == "__main__":
    root1, root2 = Node(1), Node(1)
    nodes1, nodes2 = [root1], [root2]
    nums = list(range(2, 8))
    while nums:
        n1 = nodes1.pop(0)
        n1.left = Node(nums[0])
        n1.right = Node(nums[1])
        nodes1.append(n1.left)
        nodes1.append(n1.right)

        n2 = nodes2.pop(0)
        n2.left = Node(nums[0])
        n2.right = Node(nums[1])
        nodes2.append(n2.left)
        nodes2.append(n2.right)

        nums.pop(0)
        nums.pop(0)

    print("原tree:")
    cat(root1)

    root1 = solution(root1)
    root2 = solution1(root2)

    print("递归反转:")
    cat(root1)

    print("迭代反转:")
    cat(root2)

    test(root1, root2)
