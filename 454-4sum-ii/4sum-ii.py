class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        num1_2Dict = {}
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i]+nums2[j]) in num1_2Dict:
                    num1_2Dict[nums1[i] + nums2[j]]+=1
                else:
                    num1_2Dict[nums1[i] + nums2[j]] = 1
            
        for n in range(len(nums3)):
            for m in range(len(nums4)):
                sum3_4 = -(nums3[n]+nums4[m])
                if sum3_4 in num1_2Dict:
                    count+=num1_2Dict[sum3_4]
        return count


        