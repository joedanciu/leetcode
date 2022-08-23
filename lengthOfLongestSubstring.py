class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        subString = ''
        allSubstrings = []
        length = 0
        
        for startingPoint in range( len(s) ):
            secondItter = startingPoint + 1
            subString = str( s[startingPoint] )
            
            while secondItter < len(s):
                if str( s[secondItter] ) in subString:
                    allSubstrings.append( subString )
                    break
                else:
                    subString += str( s[secondItter] )
                secondItter += 1
            allSubstrings.append( subString )
            
        for x in allSubstrings:
            if len(x) > length:
                length = len(x)
        return length
