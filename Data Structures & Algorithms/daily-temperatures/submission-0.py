class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                cur = stack.pop() # pops from back of list
                ans[cur[1]] = i - cur[1]
            stack.append([temp, i])
        return ans