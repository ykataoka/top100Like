class Solution(object):
    tmp = 0
    
    def convertBST(self, root):
        """
        The solution is rever in-order traversal.
        In every root component, increment the value and add to the value.
        """
        if root:
            # right
            self.convertBST(root.right)
            
            # root
            self.tmp += root.val
            root.val = self.tmp

            # left
            self.convertBST(root.left)

        return root
