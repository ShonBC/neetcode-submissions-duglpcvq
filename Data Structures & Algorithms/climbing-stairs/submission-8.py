class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one = 1
        two = 2
        for i in range(1, n):
            temp = two
            two += one
            one = temp
            print(one, two)
        return one