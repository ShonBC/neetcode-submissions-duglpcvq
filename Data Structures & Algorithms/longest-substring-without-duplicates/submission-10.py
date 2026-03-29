class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            ans = max(ans, i - l + 1)
        return ans