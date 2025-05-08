class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left , right = 0, len(letters) - 1
        result = ""
        while left <= right:
            mid = (left + right)//2
            if letters[mid] > target:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        return result if result else letters[0]