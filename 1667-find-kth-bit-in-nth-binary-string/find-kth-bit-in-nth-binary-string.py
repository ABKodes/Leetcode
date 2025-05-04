class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Calculate the length of the sequence S_n
        length = 2 ** n - 1
        
        # Helper function to find the k-th bit recursively
        def helper(length, k):
            # If sequence length is 1, the only bit is "0"
            if length == 1:
                return "0"
            
            # Calculate the middle point of the sequence
            half = length // 2
            
            # If k lies in the first half, recurse on the first half
            if k <= half:
                return helper(half, k)
            
            # If k lies in the second half, map to the first half and invert the result
            elif k > half + 1:
                result = helper(half, 1 + length - k)
                return "0" if result == "1" else "1"
            
            # If k is the middle bit, it is always "1"
            else:
                return "1"
        
        # Call the helper function with the initial sequence length and k
        return helper(length, k)