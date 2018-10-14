# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        t = []
        while l1 != None or l2 != None:
            if l1 != None:
                t.append(l1.val)
                l1 = l1.next
            if l2 != None:    
                t.append(l2.val)
                l2 = l2.next
        t = sorted(t)
        l3 = ListNode(t[0])
        l = l3
        for i in range(1,len(t)):
            l3.next = ListNode(t[i])
            l3 = l3.next
        return l        
        