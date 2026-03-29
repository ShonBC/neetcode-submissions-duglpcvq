class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n) n = len(numbers)
        Space Complexity: O(1)
        """
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total < target:
                L += 1
            elif total > target:
                R -= 1
            else:
                return [L + 1, R + 1]