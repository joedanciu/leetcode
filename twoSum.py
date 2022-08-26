class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        slow = 0
        for slow in range(len(nums)):
            if nums[slow] > target:
                pass
            for fast in range(slow + 1, len(nums)):
                if nums[fast] > target:
                    pass
                if (nums[slow] + nums[fast] == target):
                    return [slow, fast]
