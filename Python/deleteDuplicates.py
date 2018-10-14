# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        while self.val != None:
            res.append(str(self.val))
            self = self.next
            if not self:
                break
        return ', '.join(res)


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    l = head
    if not head:
        return l
    while head.val != None:
        if head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        if not head or not head.next:
            break
    return l


if __name__ == '__main__':
    h = ListNode(1)
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(1)
    l4 = ListNode(1)
    h.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    print(h)
    print(deleteDuplicates(h))
