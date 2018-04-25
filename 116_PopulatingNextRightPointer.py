# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        # corner case
        if not root:
            return

        level_q = [root]  # store nodes at each level
        ans = []  # store the answer value for debug
        
        while level_q != []:

            # compute something for each node in level_q
            ans.append([node.val for node in level_q if node != None])
            for i in range(len(level_q)-1):
                level_q[i].next = level_q[i+1]
            level_q[-1].next = None

            # update the next level
            next_level = []
            for node in level_q:
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            level_q = next_level
