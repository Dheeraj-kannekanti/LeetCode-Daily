class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if
                if (stack[-1]=='('and ch==')') or (stack[-1]=='{'and ch=='}') or (stack[-1]=='[' and ch==']'):
                    stack.pop()
        return len(stack)==0 


        