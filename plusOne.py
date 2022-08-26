class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lastIndex = len(digits) - 1
        index = lastIndex
        while index >= 0:
            if digits[index] < 9:
                digits[index] = digits[index] + 1
                return digits
            digits[index] = 0
            
            if index == 0:
                digits.insert(index, 1)
                return digits
            index = index - 1
