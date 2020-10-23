# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        ret = [str(root.val)]
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        if left:
            ret.append(left)
        if right:
            ret.append(right)
        return ",".join(ret)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """ 
        if not data:
            return None
        nodes = [int(n) for n in data.split(",")]
        root = self.buildTree(nodes)
        return root

    def buildTree(self, nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        i = 1
        while i < len(nodes) and nodes[i] < root.val:
            i += 1
        root.left = self.buildTree(nodes[1:i])
        root.right = self.buildTree(nodes[i:])
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans