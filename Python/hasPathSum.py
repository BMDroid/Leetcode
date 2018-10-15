# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root != None and root.left == None and root.right == None:
            return sum == root.val
        elif root != None:
            return Solution.hasPathSum(self, root.left, sum - root.val) or Solution.hasPathSum(self, root.right, sum - root.val)
        return False


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    l1 = TreeNode(4)
    l2 = TreeNode(8)
    l3 = TreeNode(11)
    l4 = TreeNode(13)
    l5 = TreeNode(4)
    l6 = TreeNode(7)
    l7 = TreeNode(2)
    l8 = TreeNode(1)
    root.left = l1
    root.right = l2
    l1.left = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    l5.right = l8
    sum = 22
    print(solution.hasPathSum(root, sum))
    r = TreeNode(1)
    l = TreeNode(2)
    r.left = l
    s = 1
    print(solution.hasPathSum(r, s))
    rNone = TreeNode(None)
    print(solution.hasPathSum(rNone, 0))
