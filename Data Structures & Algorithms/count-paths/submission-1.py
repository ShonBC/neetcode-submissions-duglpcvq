class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ''' 
        paths[m][n] = paths[m + 1][n] + paths[m][n + 1]
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        '''
        paths = [1 for i in range(n)]
        for i in range(m - 1):
            for j in range(n - 1, -1, -1):
                if j + 1 < n:
                    paths[j] += paths[j + 1]
                else:
                    paths[j] = 1
            print(paths)
        return paths[0]