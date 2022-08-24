class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningTotal = 0
        for x in range(len(nums)):
            runningTotal += nums[x]
            nums[x] = runningTotal
        return nums
