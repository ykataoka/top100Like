# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        key 1: use the dummy variable to save the first node.(starting point)
        key 2: if either l1 or l2 becomes None, then deal with the last node as an exeption
        """
        dummy = cur = ListNode(0)  # starting node

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        # In the end, add the None to the cur
        if l1 != None:
            cur.next = l1
        else:
            cur.next = l2

        # return the starting point by using dummy variable
        return dummy.next
