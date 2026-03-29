class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time Complexity: O(n) n = len(s)
        Space Complexity: O(m) m = number of unique chars in s
        '''

        window = {}
        L, ans, maxfound = 0, 0, 0
        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            maxfound = max(maxfound, window[s[R]])
            while (R - L + 1) - maxfound > k:
                window[s[L]] -= 1
                L += 1
            ans = max(ans, R - L + 1)
        
        return ans