# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute length and locate the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Connect tail to head to form a circular list
        tail.next = head

        # Step 3: Find the effective rotation shift
        k = k % length
        steps_to_new_tail = length - k

        # Step 4: Traverse to the new tail
        new_tail = tail
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 5: Set the new head and break the circular connection
        new_head = new_tail.next
        new_tail.next = None

        return new_head