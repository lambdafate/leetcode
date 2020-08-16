class Solution:
    def verifyPostorder(self, postorder):
        if len(postorder) < 3:
            return True
        root = postorder.pop()
        index = -1
        for i in range(len(postorder)):
            if postorder[i] > root:
                index = i
                break
        if index == -1:
            return self.verifyPostorder(postorder)
        # make sure that nums(after index) bigger than root
        for i in range(index, len(postorder)):
            if postorder[i] < root:
                return False
        return self.verifyPostorder(postorder[:index]) and self.verifyPostorder(postorder[index:])


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]
    Solution().verifyPostorder(test)
