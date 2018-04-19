# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        """
        if root is None:
            return 0

        # option 1: max diameter in the left sub-tree
        left_diameter = self.diameterOfBinaryTree(root.left)

        # option 2: max diameter in the right sub-tree
        right_diameter = self.diameterOfBinaryTree(root.right)

        # option 3: the path through the root
        left_num_nodes = self.normal_depth(root.left)
        right_num_nodes = self.normal_depth(root.right)

        # take the max value of above 3 options
        return max(left_diameter, right_diameter, left_num_nodes + right_num_nodes)

    def normal_depth(self, node):
        """
           1
         2   3
        4 5
        In this case, 3
        normal_depth(node(2)) = 2
        normal_depth(node(3)) = 1, 
        Thus, normal_depth(node(2)) + normal_depth(node(3)) corresponds to the diameter path.
        """
        if node is None:
            return 0
        d = 1 + max(self.normal_depth(node.left), self.normal_depth(node.right))
        return d
