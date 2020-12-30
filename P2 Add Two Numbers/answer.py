# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        pr = result
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod((pr.val + val1 + val2), 10)
            
            pr.val = val
            if not ((l1 is None or l1.next is None) and (l2 is None or l2.next is None) and carry == 0):
                pr.next = ListNode(carry)
            pr = pr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result
