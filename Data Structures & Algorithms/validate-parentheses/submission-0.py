class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ValuesCloth = {
            ")" : "(" ,
            "]" : "[" ,
            "}" : "{" }

        for c in s:
            if c in ValuesCloth:
                if stack and stack[-1] == ValuesCloth[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                





        