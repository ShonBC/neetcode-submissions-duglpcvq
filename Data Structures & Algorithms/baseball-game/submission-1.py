class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == '+':
                total = score[-1] + score[-2]
                score.append(total)
            elif op == 'D':
                score.append(score[-1] * 2)
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        ans = 0
        for val in score:
            ans += val
        return ans