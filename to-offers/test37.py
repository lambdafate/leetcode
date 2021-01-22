from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        d = deque()
        d.append(root)
        while d:
            node = d.popleft()
            if node:
                ans.append(str(node.val))
                d.append(node.left)
                d.append(node.right)
            else:
                ans.append("null")
        while ans and ans[-1] == "null": ans.pop()
        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data[1:len(data)-1].split(",")
        root = TreeNode(int(data[0]))
        d = deque()
        d.append(root)
        i = 1
        while i < len(data):
            node = d.popleft()
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                d.append(node.left)
            i += 1
            if i < len(data) and data[i] != "null":
                node.right = TreeNode(int(data[i]))
                d.append(node.right)
            i += 1
        return root




"""
class Codec:

    def serialize(self, root):
        if not root:
            return ""
        ans = []
        d = deque()
        d.append(root)
        while d:
            flag = True
            for _ in range(len(d)):
                node = d.popleft()
                ans.append(str(node.val) if node else "null")
                if node:
                    d.append(node.left)
                    d.append(node.right)
                    if node.left or node.right:
                        flag = False
                else:
                    d.append(None)
                    d.append(None)
            if flag: break
        while ans and ans[-1] == "null": ans.pop()
        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        if not data:
            return None
        data = data[1:len(data)-1].split(",")
        root = TreeNode(int(data[0]))
        d = deque()
        d.append(root)
        i = 1
        while i < len(data):
            for _ in range(len(d)):
                if i >= len(data): break
                node = d.popleft()
                if node:
                    node.left = None if i >= len(data) or data[i] == "null" else TreeNode(int(data[i]))
                    node.right = None if i + 1 >= len(data) or data[i+1] == "null" else TreeNode(int(data[i+1]))
                i += 2
                if node:
                    d.append(node.left)
                    d.append(node.right)
                else:
                    d.append(None)
                    d.append(None)
        return root
"""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

