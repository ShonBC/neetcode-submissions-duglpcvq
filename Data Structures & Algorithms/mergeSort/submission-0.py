# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def split(pairs, s, e):
            if e - s + 1 <= 1:
                return pairs
            m = (s + e) // 2
            split(pairs, s, m)
            split(pairs, m + 1, e)

            merge(pairs, s, m, e)
            return pairs
        
        def merge(pairs, s, m, e):
            l = pairs[s:m+1]
            r = pairs[m+1:e+1]
            i = j = 0
            k = s
            while i < len(l) and j < len(r):
                if l[i].key <= r[j].key:
                    pairs[k] = l[i]
                    i += 1
                else:
                    pairs[k] = r[j]
                    j += 1
                k += 1
            while i < len(l):
                pairs[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                pairs[k] = r[j]
                j += 1
                k += 1


        return split(pairs, 0, len(pairs) - 1)
