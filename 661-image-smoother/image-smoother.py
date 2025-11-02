class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                res[i][j] = total // count
        return res