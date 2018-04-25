# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        Approach: write an example tree and compute preorder and inorder.
        Then, try to find the rule.
        When construncting, anyway it is going to be recursive approach.
        """
        # base case
        if preorder == []:
            return

        # recursive
        root_val = preorder.pop(0)
        idx = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[:idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx:], inorder[idx+1:])
        return root   
