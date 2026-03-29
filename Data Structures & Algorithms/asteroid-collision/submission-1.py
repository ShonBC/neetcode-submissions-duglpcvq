class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for val in asteroids: 
            while ans and val < 0 and ans[-1] > 0:
                diff = val + ans[-1]
                if diff < 0:
                    ans.pop()
                elif diff > 0:
                    val = 0
                else:
                    ans.pop()
                    val = 0
            if val:
                ans.append(val)
        return ans