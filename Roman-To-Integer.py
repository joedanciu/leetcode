class Solution(object): 
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            if romanNum[s[i]] < romanNum[s[i+1]]:
                total = total + (romanNum[s[i+1]]-romanNum[s[i]])
            else: 
                total = total + romanNum[s[i]]
        return total

'''romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if romanNum[s[i]] < romanNum[s[j]]:
                    beingAdded = (romanNum[s[i+1]]-romanNum[s[i]])
                    total = total + beingAdded
                    print("Detected " + str(romanNum[s[i+1]]) + "minus" + str(romanNum[s[i]]) + "so adding" + str(beingAdded))
                else: 
                    beingAdded = romanNum[s[i]]
                    total = total + beingAdded
                    print("Detected " + str(romanNum[s[i]]) +  "so adding" + str(beingAdded))
        return total'''