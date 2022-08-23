# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        outputArray = []
        headDup = head
        while headDup != None and headDup.next != None:
            if headDup.next.val != 0:
                count = count + headDup.val
                headDup = headDup.next
            else:
                count = count + headDup.val
                outputArray.append(count)
                headDup = headDup.next
                count = 0
        
        returnOutput = ListNode()
        mutPointer = returnOutput
        for x in outputArray:
            mutPointer.next = ListNode(x)
            mutPointer = mutPointer.next

        return returnOutput.next
