# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast, slow = head, head.next

        try:
            while fast != slow:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
