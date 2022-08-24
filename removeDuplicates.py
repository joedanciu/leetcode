class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index1, index2, total = 0, 1, 1
        
        while index2 in range(len(nums)):
            if nums[index1] == nums[index2]:
                index2 += 1
                nums[index1+1] = "_"
            else:
                nums[index1+1] = nums[index2]
                index2 += 1
                index1 += 1
        total = total + index1
        return total

    """ BEST SLOW/FAST METHOD STUDY THIS
		slow = 0
		for fast in range(1, len(nums)):
			if nums[slow] != nums[fast]:
				slow += 1
				nums[slow] = nums[fast]
		return slow + 1
    """
