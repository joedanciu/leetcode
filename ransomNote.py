class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomLength = len(ransomNote)
        counter = 0
        
        for x in range(len(ransomNote)):
            if ransomNote[x] in magazine:
                magazine = magazine.replace(ransomNote[x], '', 1)
                counter = counter + 1   
        return (ransomLength == counter)
