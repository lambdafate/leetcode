# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        nodes = []
        self.inorderToList(root, nodes)
        if not nodes:
            return None
        # fix mid
        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i+1].left = nodes[i]
        # fix head and tail
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        return nodes[0]
    
    def inorderToList(self, root, result):
        if root is None:
            return
        self.inorderToList(root.left, result)
        result.append(root)
        self.inorderToList(root.right, result)



    def treeToDoublyList2(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            root.left, root.right = root, root
            return root

        left_nodes = self.treeToDoublyList(root.left)
        right_nodes = self.treeToDoublyList(root.right)
        root.left, root.right = root, root

        head = left_nodes if left_nodes is not None else root
        if right_nodes is not None:
            root.left, right_nodes.left.right = right_nodes.left, root
            root.right, right_nodes.left = right_nodes, root
        if left_nodes is not None:
            tail = root.left
            # fix mid
            left_nodes.left.right, root.left = root, left_nodes.left
            # fix head and tail
            left_nodes.left, tail.right = tail, left_nodes
        return head


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    res = Solution().treeToDoublyList(root)
    head = res
    while res:
        print(res.val)
        res = res.right
        if res == head:
            break
