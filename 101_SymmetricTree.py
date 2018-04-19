# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.inOrder = []
        self.reverseInOrder = []

    def InOrderTraversal(self, root):
        if root is None:
            self.inOrder.append(None)
            return
        # left
        self.InOrderTraversal(root.left)
        # root
        self.inOrder.append(root.val)
        # right
        self.InOrderTraversal(root.right)

    def ReverseInOrderTraversal(self, root):
        if root is None:
            self.reverseInOrder.append(None)
            return
        # right
        self.InOrderTraversal(root.right)
        # root
        self.reverseInOrder.append(root.val)
        # left
        self.InOrderTraversal(root.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # run the Inorder traversal
        self.InOrderTraversal(root)
        # run the ReverseInorder traversal
        self.ReverseInOrderTraversal(root)

        print(self.inOrder)
        print(self.reverseInOrder)
        
        # Check if the outcome is same or not
        lengthArray = len(self.inOrder)
        for i in range(lengthArray):
            if self.inOrder[i] != self.reverseInOrder[i]:
                return False
        return True
        
#class Solution(object):
#    def __init__(self):
#        self.leftOrder = []
#        self.rightOrder = []
#        
#    def postLeftOrder(self, root):
#        if root.left != None:
#            self.postLeftOrder(root.left)
#        if root.right != None:
#            self.postLeftOrder(root.right)
#        self.leftOrder.append(root.val)
#        
#    def postRightOrder(self, root):
#        if root.right != None:
#            self.postRightOrder(root.right)
#        if root.left != None:
#            self.postRightOrder(root.left)
#        self.rightOrder.append(root.val)
#
#    def isSymmetric(self, root):
#        """
#        :type root: TreeNode
#        :rtype: bool
#        """
#        if not root:
#            return
#        self.postLeftOrder(root)
#        self.postRightOrder(root)
#        if self.leftOrder[::-1] == self.rightOrder:
#            return True
#        else:
#            return False
