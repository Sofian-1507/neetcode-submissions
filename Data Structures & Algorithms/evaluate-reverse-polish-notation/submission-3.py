class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        for char in tokens : 
            if char == "+":
                x=stack.pop()
                y=stack.pop()
                ans =x+y
                stack.append(ans)
            elif char == "-":
                x=stack.pop()
                y=stack.pop()
                ans =y-x
                stack.append(ans)
            elif char == "*":
                x=stack.pop()
                y=stack.pop()
                ans = y*x
                stack.append(ans)
            elif char == "/":
                x=stack.pop()
                y=stack.pop()
                ans = int(y/x)
                stack.append(ans)
            else:
                stack.append(int(char))
        
        return stack[-1]