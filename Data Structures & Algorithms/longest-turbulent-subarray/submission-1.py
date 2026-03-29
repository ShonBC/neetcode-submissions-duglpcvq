class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        Time Complexity: O(n) n is len(arr)
        Space Complexity: O(1) constant space
        '''
        turb = ''
        l, r = 0, 1
        ans = 1
        while r < len(arr):
            if turb != '>' and arr[r - 1] > arr[r]:
                ans = max(ans, r - l + 1)
                r += 1
                turb = '>'
            elif turb != '<' and arr[r - 1] < arr[r]:
                ans = max(ans, r - l + 1)
                r += 1
                turb = '<'
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                turb = ''
        
        return ans