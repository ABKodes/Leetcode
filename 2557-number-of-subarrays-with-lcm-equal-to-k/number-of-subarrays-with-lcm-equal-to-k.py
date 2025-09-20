class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            lcm = 1
            for j in range(i, n):
                if k % nums[j] != 0:
                    break
                lcm = lcm * nums[j] // gcd(lcm, nums[j])
                if lcm > k:
                    break
                if lcm == k:
                    ans += 1
        return ans