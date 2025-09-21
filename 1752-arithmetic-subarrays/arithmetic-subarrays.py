class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            lst = nums[left: right+1]
            lst.sort()
            gap = lst[1] - lst[0]
            # print(lst)
            for i in range(len(lst)-1):
                if lst[i+1] - lst[i] != gap:
                    output.append(False)
                    break
            else:
                output.append(True)
        return output
                    