# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p = root
        insert = False
        while not insert:
            if p.val < val:
                if p.right is None:
                    p.right = TreeNode(val)
                    insert = True
                    break
                p = p.right
            else:
                if p.left is None:
                    p.left = TreeNode(val)
                    insert = True
                    break
                p = p.left
        return root
