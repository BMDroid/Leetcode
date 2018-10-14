# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        p = self
        while p != None:
            res.append(str(p.val))
            p = p.next
        return ', '.join(res)


class Solution:
    def deleteNode(self, head, node):
        """
        :type head: ListNode
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if head.val == node.val:
            head = head.next
        else:
            delete = False
            p = head
            while not delete:
                q = p.next
                if q.val == node.val:
                    p.next = q.next
                    delete = True
                p = p.next


if __name__ == '__main__':
    head = ListNode(4)
    l1 = ListNode(1)
    l2 = ListNode(5)
    l3 = ListNode(9)
    head.next = l1
    l1.next = l2
    l2.next = l3
    print(head)
    s = Solution()
    s.deleteNode(head, l3)
    print(head)
