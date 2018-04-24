# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isMatch(self, s, t):
        
        # if s == None and t == None, True
        # if s == None and t != None, False
        # if s != None and t == None, False
        # else, proceed to next
        if (s is None) or (t is None):
            return s == t

        return (s.val == t.val and
                self.isMatch(s.left, t.left) and
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Check if the current S and T matches
        if self.isMatch(s, t):
            return True

        # if the candidate of the subtree is None, return False (as s.left or s.right will be error)
        if s is None:
            return False

        # The chance still exists. Proceed to next step.
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
