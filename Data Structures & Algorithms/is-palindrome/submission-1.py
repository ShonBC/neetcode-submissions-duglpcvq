class Solution:
    def isPalindrome(self, s: str) -> bool: 
        '''
        Time Complexity: O(n)
        Space Complexity: O(n) n = len(s)
        '''
        ans = ''
        for c in s:
            if c.isalnum():
                ans += c.lower()
        return ans == ans[::-1]
