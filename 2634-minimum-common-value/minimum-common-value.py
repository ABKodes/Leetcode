class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0
        counter = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                counter = nums1[first]
                break
            elif nums1[first] < nums2[second]:
                first += 1
            else:
                second += 1
        return -1 if counter == 0 else counter