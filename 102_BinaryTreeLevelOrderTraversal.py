class Solution(object):

    # Preorder Traversal with the queue
    def levelOrder(self, root):
        if root == None or root == []:
            return []
        ans = []
        level = [root]  # store the nodes in the same level. initialized at the first level.
        while level != []:
            # 1. add the node to answer from each level
            ans.append([node.val for node in level])
            # 2. add the next level node(node.left, node.right) to level
            tmp = []
            for node in level:
                if node.left != None:
                    tmp.extend([node.left])
                if node.right != None:
                    tmp.extend([node.right])
            level = tmp

        return ans
