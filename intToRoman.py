class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        outputString = ''
        romanVal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanNum = ['M', 'CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
       
        index = 0
        while index < len(romanVal):
            if (num - romanVal[index]) >= 0:
                outputString = outputString + romanNum[index]
                num = num - romanVal[index]
            else: 
                index = index + 1
        return outputString 
