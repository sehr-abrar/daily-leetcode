# 2. Medium: Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # loop through both lists until both are exhausted
        while l1 or l2 or carry:
            # get the values from l1 and l2, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # create a new node with the digit and move forward
            current.next = ListNode(digit)
            current = current.next

            # move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # return the result list, skipping the dummy node
        return dummy.next
