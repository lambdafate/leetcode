import queue as Queue

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
        ret = []
        queue = Queue.Queue()
        queue.put(root)
        while queue:
            level = []
            flag = False
            for _ in range(queue.qsize()):
                tmp = queue.get()
                if tmp:
                    queue.put(tmp.left)
                    queue.put(tmp.right)
                    level.append(str(tmp.val))
                    flag = True
                else:
                    queue.put(None)
                    queue.put(None)
                    level.append('null')
            if not flag:
                break
            ret.extend(level)
        if len(ret) == 0:
            ret.append('null')
        return "[" + ",".join(ret) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data[1:-1]
        ret = data.split(",")
        root = None if ret[0] == 'null' else TreeNode(ret[0])
        if root is None:
            return root
        queue = Queue.Queue()
        queue.put(root)
        i = 1
        while i < len(ret):
            for _ in range(queue.qsize()):
                tmp = queue.get()
                if tmp:
                    if ret[i] != 'null':
                        tmp.left = TreeNode(int(ret[i]))
                    if ret[i+1] != 'null':
                        tmp.right = TreeNode(int(ret[i+1]))
                    queue.put(tmp.left)
                    queue.put(tmp.right)
                else:
                    queue.put(None)
                    queue.put(None)
                i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
