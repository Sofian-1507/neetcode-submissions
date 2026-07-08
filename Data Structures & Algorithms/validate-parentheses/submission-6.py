class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        i = 0
        while i < len(s):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                stack.append(s[i])
            else:
                if not stack : 
                    return False
                elif s[i]=="}" and stack[-1]=="{" :
                    stack.pop()  
                elif s[i]==")" and stack[-1]=="(" :
                    stack.pop()  
                elif s[i]=="]" and stack[-1]=="[" :
                    stack.pop()
                else : 
                    return False  
            i+=1
        return len(stack)== 0

        
              