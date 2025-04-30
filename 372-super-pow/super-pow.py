class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        for digit in b:
            result = ((result ** 10) * (a**digit % 1337)) % 1337
        return result