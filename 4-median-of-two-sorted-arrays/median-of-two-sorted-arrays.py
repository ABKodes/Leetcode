class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1 + nums2)
        half = len(result)//2
        return result[half] if len(result) %2 != 0 else (result[half] + (result[half - 1]))/2