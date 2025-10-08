class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if not b:
            return 0
    
        if b in a:
            return 1
        rep = (len(b) + len(a) - 1) // len(a)
        repeated = a * rep
        if b in repeated:
            return rep

        repeated += a 
        if b in repeated:
            return rep + 1
        
        return -1