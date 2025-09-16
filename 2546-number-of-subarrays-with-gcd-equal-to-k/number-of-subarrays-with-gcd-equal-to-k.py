class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for left in range(len(nums)):
            temp = nums[left]
            if temp == k:
                count +=1
            for right in range(left + 1,len(nums)):
                temp = gcd(temp,nums[right])
                if temp == k:
                    count += 1
        return count