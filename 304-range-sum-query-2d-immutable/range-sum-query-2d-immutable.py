class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, columns = len(matrix), len(matrix[0])
        # Prefix Sum
        self.prefixSum = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for column in range(columns):
                self.prefixSum[row + 1][column + 1] = (
                    (self.prefixSum[row + 1][column] + self.prefixSum[row][column + 1])
                    - self.prefixSum[row][column]
                    + matrix[row][column]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row1][col2 + 1]
            - self.prefixSum[row2 + 1][col1]
            + self.prefixSum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
