# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return ' -> '.join(values)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

def list_to_likedlist(lst):
    dummy = ListNode()
    current = dummy
    for i in lst:
        current.next = ListNode(i)
        current = current.next
#    print(dummy)
    return dummy.next
    
l1 = list_to_likedlist([2, 4, 3])
print(l1)
l2 = list_to_likedlist([5, 6, 4])
print(l2)
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print(result)