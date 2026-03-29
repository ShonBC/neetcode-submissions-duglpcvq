# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        start = 0
        end = len(pairs) - 1

        def split(pairs, s, e):
            if s >= e:
                return
            pivot = pairs[e]
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    temp = pairs[i]
                    pairs[i] = pairs[left]
                    pairs[left] = temp
                    left += 1
            pairs[left], pairs[e] = pairs[e], pairs[left]
            split(pairs, s, left - 1)
            split(pairs, left + 1, e)
        split(pairs, start, end)
        return pairs

