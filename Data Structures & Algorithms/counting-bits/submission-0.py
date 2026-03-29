class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        ans = []
        for i in range(n + 1):
            cur = i
            count = 0
            while cur > 0:
                count = count + 1 if cur & 1 == 1 else count
                cur = cur >> 1
            ans.append(count)
        return ans