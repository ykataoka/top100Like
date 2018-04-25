# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        ans = []
        level_q = [root]
        level_val = 1

        while level_q != []:
            level_q = [node for node in level_q if node != None]
#            level_q_val = [node.val for node in level_q if node != None]
            self.bfs(level_q, ans, level_val)
            level_val += 1
        return ans
    
    def bfs(self, level_q, ans, level_val):

        ans_tmp = []
        level_tmp = []
        # for each node at specific level
        while level_q != []:
            node = level_q.pop()
            ans_tmp.append(node.val)

            # even level_q
            if level_val % 2 == 1:
                if node.left != None:
                    level_tmp.append(node.left)
                if node.right != None:
                    level_tmp.append(node.right)
            # odd level_q
            else:
                if node.right != None:
                    level_tmp.append(node.right)
                if node.left != None:
                    level_tmp.append(node.left)
        ans.append(ans_tmp)
        for node in level_tmp:
            level_q.append(node)
