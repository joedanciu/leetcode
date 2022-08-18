class Solution(object): 
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(0, len(s)-1):
            if romanNum[s[i]] < romanNum[s[i+1]]:
                total = total - romanNum[s[i]]
                i = i + 2
            else: 
                total = total + romanNum[s[i]]
                i = i + 1
        return total + romanNum[s[-1]]
