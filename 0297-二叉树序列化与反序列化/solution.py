from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[null]"
        ret = []
        queue = deque([root])
        curr, last = None, root
        while last is not curr:
            curr = queue.popleft()
            if curr:
                ret.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
                last = curr.right or curr.left or last
            else:
                ret.append('null')
                queue.append(None)
                queue.append(None)

        return "[" + ",".join(list(ret)) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data[1:-1].split(",")
        root = None if values[0] == 'null' else TreeNode(int(values[0]))
        if root is None:
            return None
        queue = deque([root])
        i = 1
        while i < len(values):
            curr = queue.popleft()
            if curr:
                if values[i] != 'null':
                    curr.left = TreeNode(int(values[i]))
                if i + 1 >= len(values):
                    break
                if values[i+1] != 'null':
                    curr.right = TreeNode(int(values[i+1]))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                queue.append(None)
                queue.append(None)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
