class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num1 in nums:
            num2 = target - num1
            index = nums.index(num1)
            length = len(nums)
            for i in range(index + 1, length):
                if nums[i] == num2:
                    return [index, i]
 