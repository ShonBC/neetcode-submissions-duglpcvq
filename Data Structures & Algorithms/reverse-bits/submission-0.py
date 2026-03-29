class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Time and Space Complexity: O(1) constant.
        '''
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1 # Check if ith bit of n is 1
            ans += (bit << (31 - i)) # place the ith bith value it 31 - i bit of ans
        return ans 