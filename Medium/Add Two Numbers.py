# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        reference = curr
        
        carry = 0
        while l1 or l2 or carry:
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0
            
            num = first_num + second_num + carry
            carry = num // 10
            num = num % 10
            
            #set the next node in the linked list
            reference.next = ListNode(num)
            
            #go to the next node in the linked list
            reference = reference.next
            
            # if next l1 node not empty go there else set it to None, breaks while loop
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return curr.next
            