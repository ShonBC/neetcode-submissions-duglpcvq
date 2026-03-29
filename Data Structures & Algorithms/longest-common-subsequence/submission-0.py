class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        ans is matrix size iXj, i is len(text2) + 1 and j is len(text1) + 1 for 2D DP
        fill ans bottom up, if letters match -> ans cell == 1 + the diagonal down cell
        Else -> ans cell = max(down cell, right cell)
        This tracks the number of sequential matches in the string including if letters were removed.
        Time Complexity: O(i*j)
        Space Complexity: O(i*j)
        '''
        ans = [[0 for j in range(len(text1) + 1)] for i in range(len(text2) + 1)]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]:
                    ans[i][j] = 1 + ans[i + 1][j + 1]
                else:
                    ans[i][j] = max(ans[i + 1][j], ans[i][j + 1])
        return ans[0][0]