"""

思路
两个指针lessTail, greaterTail指向<x末端、>x末端
lessTail.next.val >= x

若pointer.val < x
    lessTail.next = pointer
    lessTail = pointer
    pointer = pointer.next
若pointer.val < x
    greaterTail.next = pointer
    greaterTail = pointer
    pointer = pointer.next
若pointer.val == x
    lessTail.next, pointer.next, pointer = pointer, lessTail.next, pointer.next

初始状态
lessTail, greaterTail = None, None 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessHead, greaterHead = ListNode(None), ListNode(None)
        lessTail, greaterTail = lessHead, greaterHead
        pointer = head
        while pointer:
            if pointer.val < x:
                lessTail.next = pointer
                lessTail = pointer
                pointer = pointer.next
            elif pointer.val > x:
                greaterTail.next = pointer
                greaterTail = pointer
                pointer = pointer.next
            else:
                savePN, saveGHN = pointer.next, greaterHead.next
                greaterHead.next = pointer
                pointer.next = saveGHN
                pointer = savePN

        lessTail.next = greaterHead.next
        return lessHead.next
