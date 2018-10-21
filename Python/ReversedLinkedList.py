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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        lst = []
        while head != None:
            lst.append(ListNode(head.val))
            head = head.next
        lst = lst[::-1]
        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]
        return lst[0]


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    head.next = l1
    l1.next = l2
    print(s.reverseList(head))
