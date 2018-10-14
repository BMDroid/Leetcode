# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p != None and q != None:
        if p.val == q.val:
            print(p.val, q.val)
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    elif p == None and q == None:
        return True
    return False


def isSameTree2(p, q):
    if p and q:
        return p.val == q.val and isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right)
    return p is q


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(isSameTree(p, q))
