class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque()
        ans = 0
        for i in s:
            print(i in window)
            while i in window:
                print(f'i: "{i}"', ans)
                ans = max(ans, len(window))
                window.popleft()
            window.append(i)
        return max(ans, len(window))