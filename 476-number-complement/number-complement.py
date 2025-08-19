class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        binary = (2 ** n) - 1
        return binary ^ num