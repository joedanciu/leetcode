class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        starting = strs[0]
        
        for x in strs:
            if x == "":
                return output
            if len(x) < len(starting):
                starting = x

        for x in range(len(starting)):
            counter = 0
            for z in range(len(strs)):
                if starting[x] not in strs[z][x]:
                    return output
                counter = counter + 1
                if counter == len(strs):
                    output += starting[x]
        return output
