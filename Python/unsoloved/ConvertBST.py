# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.tree = []

        def _traverse(node):
            if node is not None:
                self.tree.append(node.val)
                if node.left is not None:
                    _traverse(node.left)
                if node.right is not None:
                    _traverse(node.right)

        def _update(node, lst):
            if node is not None:
                if node.val != lst[-1]:
                    node.val += sum(lst[lst.index(node.val) + 1::])
                if node.left is not None:
                    _update(node.left, sortedTree)
                if node.right is not None:
                    _update(node.right, sortedTree)
        _traverse(root)
        sortedTree = sorted(self.tree)
        _update(root, sortedTree)
        return root

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def _update(node):
            if node is None:
                return 0
            sum_right = 0
            sum_left = 0
            if node is not None:
                if node.right is not None:
                    sum_right += node.right.val + _update(node.right)
                node.val += sum_right
                if node.left is not None:
                    sum_left += node.left.val + _update(node.left)
            return sum_right + sum_left

        def _traverse(node):
            if node is not None:
                _update(node)
                if node.left is not None:
                    _traverse(node.left)
                if node.right is not None:
                    _traverse(node.right)
        _traverse(root)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    l1 = TreeNode(2)
    l2 = TreeNode(13)
    root.left = l1
    root.right = l2
    #l3 = TreeNode(3)
    #l4 = TreeNode(4)
    #l5 = TreeNode(4)
    #l6 = TreeNode(3)
    #l1.left = l3
    #l1.right = l4
    #l2.left = l5
    #l2.right = l6
    s = Solution()
    s.convertBST(root)
