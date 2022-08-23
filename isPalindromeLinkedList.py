# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listToString = ''
        index = 0
        while head != None:
            listToString = listToString + str(head.val)
            head = head.next
            index = index + 1
        revString = listToString[::-1]
        return (revString == listToString)
