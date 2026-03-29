# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while True:
            mid = l + round((r - l) / 2)
            ret = guess(mid)
            if ret < 0:
                r = mid - 1
            elif ret > 0:
                l = mid + 1
            else:
                return mid
        