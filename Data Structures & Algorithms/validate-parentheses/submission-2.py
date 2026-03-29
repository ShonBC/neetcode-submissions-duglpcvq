class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i not in check.keys():
                if stack and i == check[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
        