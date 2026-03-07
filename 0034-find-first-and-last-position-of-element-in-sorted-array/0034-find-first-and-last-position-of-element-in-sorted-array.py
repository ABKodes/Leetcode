class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstPosition(nums, target):
            result = 0
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def lastPosition(nums, target):
            result = 0
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = firstPosition(nums, target), lastPosition(nums, target)
        if left <= right:
            return [left, right]
        return [-1, -1]
