class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Time Complexity: O(n) n = len(s)
        Space Complexity: O(m) m = # of unique characters in s
        '''
        window = set()
        L = 0
        ans = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            ans = max(ans, len(window))
        return ans