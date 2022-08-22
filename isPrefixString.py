class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """

        stringVersion = ''
        if len(words[0]) > len(s):
            return False
        for x in words:
            stringVersion = stringVersion + str( x )
        if len(stringVersion) < len(s):
            return False
        index = 0
        stringIndex = 0
        while stringIndex < len(s) and index < len(words):
            if words[index] == (s [stringIndex:len(words[ index ]) + stringIndex]):
                stringIndex = stringIndex + len(words[index]) 
                index = index + 1
            else: return False
        return True
