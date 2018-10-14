# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 1 + max(Solution.maxDepth(self, root.left),
                    Solution.maxDepth(self, root.right))
        return depth


if __name__ == '__main__':
    root = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(15)
    n4 = TreeNode(7)
    root.left = n1
    root.right = n2
    n2.left = n3
    n2.right = n4
    s = Solution()
    print(s.maxDepth(root))
