# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        an, bn = 0, 0
        tmp = headA
        while tmp!=None:
            an += 1
            tmp = tmp.next
        tmp = headB
        while tmp!=None:
            bn += 1
            tmp = tmp.next
        while an!=bn:
            if an>bn:
                headA = headA.next
                an -= 1
            else:
                headB = headB.next
                bn -= 1
        while headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA
