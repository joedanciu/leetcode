class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lastIndex = len(digits) - 1
        index = lastIndex
        while index >= 0:
            '''print("index is " + str(index))'''
            if digits[index] < 9:
                digits[index] = digits[index] + 1
                '''print(str(digits[index]) + " was less than nine so we added 1")'''
                return digits
            '''print("at index " + str(index) + " we detected a 9 so we swapped to 0")'''
            digits[index] = 0
            
            if index == 0:
                '''print(str(index) + " inserted a 1 at index")'''
                digits.insert(index, 1)
                return digits
            index = index - 1
