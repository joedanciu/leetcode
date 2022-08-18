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
        try:
            if head.val == "X":
                return True
        except AttributeError:
            return False
        head.val = "X"
        return self.hasCycle(head.next)
