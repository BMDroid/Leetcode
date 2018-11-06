# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def symmetric(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            if n1.val == n2.val:
                if symmetric(n1.left, n2.right) and symmetric(n1.right, n2.left):
                    return True
            return False
        return symmetric(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(2)
    root.left = l1
    root.right = l2
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(4)
    l6 = TreeNode(3)
    l1.left = l3
    l1.right = l4
    l2.left = l5
    l2.right = l6
    s = Solution()
    print(s.isSymmetric(root))
