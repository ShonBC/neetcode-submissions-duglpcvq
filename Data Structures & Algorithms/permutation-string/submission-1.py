class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 27
        for c in s1:
            cur = ord(c) - 96
            count1[cur] += 1

        count2 = [0] * 27
        l = r = 0
        while r < len(s2):
            count2[ord(s2[r]) - 96] += 1
            
            if count1 == count2:
                return True
            r += 1
            if r - l == len(s1):
                count2[ord(s2[l]) - 96] -= 1
                l += 1
        return False
