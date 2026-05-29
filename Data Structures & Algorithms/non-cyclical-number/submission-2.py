class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = self.sumSquares(n)
        return True

    def sumSquares(self, n: int) -> int:
        total = 0
        while n:
            print(n)
            total += (n % 10)**2
            n = n // 10
        print(total)
        return total