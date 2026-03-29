class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        left = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            ans = max(ans, len(seen))
        return ans