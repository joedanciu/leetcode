class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        stripped = s.strip()
        negativeFlag = 0
        updatedString = stripped
        finalString = ''
        bigInt = 2147483647
        
        if len(stripped) == 0:
            return 0
        if '+' == stripped[0]:
            updatedString = stripped[1:len(stripped)]
        if '-' == stripped[0]:
            negativeFlag = 1
            bigInt = 2147483648
            updatedString = stripped[1:len(stripped)]
        for x in range(len(updatedString)):
            if updatedString[ x ] in numbers:
                finalString = finalString + updatedString[ x ]
            else: break
        if finalString == '':
            return 0
        if (int(finalString) > ((2**31) - 1) ) or ( int(finalString) < (-2**31) ):
            finalString = bigInt 
        if negativeFlag == 1:
            return 0 - (int( finalString ))
        return int(finalString)
