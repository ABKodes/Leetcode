class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        chars = [str(digit) for digit in digits]
        chars = int(("").join(chars)) + 1
        chars = list(str(chars))
        chars = [int(char) for char in chars]
        return chars