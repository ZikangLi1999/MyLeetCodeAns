class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        length = len(nums)
        if length % 2 == 0:
            return (float(nums[length / 2]) + float(nums[length / 2 - 1])) / 2
        else:
            return float(int(nums[(length - 1) / 2]))
