class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ogInput = str(x)
        revInput = ogInput[::-1]
        if ogInput == revInput:
            return True
        return False
