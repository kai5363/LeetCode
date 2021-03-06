// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        dummy = l3 = ListNode(0)
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = (l2.val if l2 else 0)            
            l3.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            l3 = l3.next
        if carry > 0:
            l3.next = ListNode(carry)
        
        
            
        return dummy.next
        