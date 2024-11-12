import re
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(","]":"[","}":"{"}
        
        if len(s) % 2 != 0:
            return False
        stack = []
        for element in s:
            if element not in pairs:
                stack.append(element)
                continue 

            if not stack:
                return False
            ind = len(stack)-1
            if stack[ind] == pairs[element]:
                stack.pop(ind)
                continue
            return False
        if len(stack) == 0:
            return True
        return False


            
            
            
            

       
         
sol = Solution()
print(sol.isValid("([])"))