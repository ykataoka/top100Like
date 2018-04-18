class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Solution 1: Iteration
        # not using the recursive but using the while loop
        # prev = None
        # curr = head
        # while curr != None:
        #     tmp_next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tmp_next_node
        # return prev

        # Solution 2: Recursive
        # call the reverseList function in the reverseList function
        prev = None
        curr = head
        while curr != None:
            tmp_next_node = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next_node
        return prev

    
s = Solution()
print(s.majorityElement([4, 3, 2, 2, 2, 2, 3, 1, 2]))
print(s.majorityElement([6, 5, 5]))
print(s.majorityElement([3, 3, 4]))
