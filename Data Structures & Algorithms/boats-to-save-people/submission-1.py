class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] + people[r] > limit:
                if people[r] <= limit:
                    ans += 1
                r -= 1
            else:
                l += 1
                r -= 1
                ans += 1
        return ans