class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity: O(row*col)
        Space Complexity: O(row*col)
        '''
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        paths = [[0] * col for i in range(row)]
        if obstacleGrid[row - 1][col - 1] == 1:
            return 0

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                elif i == row - 1 and j == col - 1:
                    paths[i][j] = 1
                else:
                    right = paths[i][j + 1] if j + 1 <= col - 1 else 0
                    down = paths[i+1][j] if i + 1 <= row - 1 else 0
                    paths[i][j] = down + right
        return paths[0][0]        