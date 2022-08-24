class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stringVer = str(x)
        nonNegative = ''
        flag = 0

        if stringVer[0] == '-':
            flag = 1
            nonNegative = stringVer[1:len(stringVer)]
            reversedString = nonNegative[::-1]
        else:
            reversedString = stringVer[::-1]
        
        reversedNumber = int(reversedString)
        
        if reversedNumber > ( (2**31) - 1 ) or reversedNumber < (-2**31) or len(str(x)) == 0:
            return 0
        if flag:
            return 0 - reversedNumber
        return reversedNumber
