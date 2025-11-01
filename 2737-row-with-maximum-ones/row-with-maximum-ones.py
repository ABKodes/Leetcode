class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max = 0
        ind = 0

        for i, row in enumerate(mat):
            count = row.count(1)
            if count > max:
                max = count
                ind = i
        return [ind, max]