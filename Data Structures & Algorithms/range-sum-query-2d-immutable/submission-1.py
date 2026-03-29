class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''
        Prefix sum instantiation is O(m*n) Time and Space Complexity 
        where m is the # of rows and n is # of cols
        '''
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        self.pre = [[0] * col for _ in range(row)]
        # Define prefix sum
        for i in range(len(matrix)): # row
            total = 0
            for j in range(len(matrix[i])): # col
                total += matrix[i][j]
                print(i,j,self.pre)
                self.pre[i][j] = total
        print(self.pre)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        Time Complexity: O(i) i = row2 - row1
        Space Complexity: O(1)
        '''
        rowsum = 0
        for i in range(row1, row2 + 1):
            Rsum = 0
            Lsum = 0
            Rsum += self.pre[i][col2]
            Lsum += self.pre[i][col1 - 1] if col1 > 0 else 0
            rowsum += Rsum - Lsum
        print(Rsum, Lsum, rowsum)
        return rowsum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)