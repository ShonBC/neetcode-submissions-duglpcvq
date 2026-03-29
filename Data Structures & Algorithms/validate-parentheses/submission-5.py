class Solution:
    def isValid(self, s: str) -> bool:
        check = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for i in s:
            if i in check:
                if stack and stack[-1] == check[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
