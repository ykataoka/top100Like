class Solution():
    def InvertTree(self, root):
        if root is None:
            return
        # PreOrder Traversal should be good?

        # 1. swap the left and right node
        # 2. apply inverTree for the left node
        # 3. apply inverTree for the right node
        root.left, root.right = root.right, root.left
        root.left = self.InvertTree(root.left)
        root.right = self.InvertTree(root.right)
        return root
