class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        powerOf2s = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '131072', '262144', '524288', '1048576', '2097152', '4194304', '8388608', '16777216', '33554432', '67108864', '134217728', '268435456', '536870912', '1073741824', '2147483648', '4294967296', '8589934592']
        
        inputNum = str(n)
        for x in range(len(powerOf2s)):
            if len(powerOf2s[x]) == len(inputNum):
                flag = 0
                tempNumber = powerOf2s[x]
                for z in range(len(inputNum)):
                    if inputNum[z] in tempNumber:
                        tempNumber = tempNumber.replace(inputNum[z], '_', 1) 
                        flag += 1
                if flag == len(inputNum):
                    return True
        return False
