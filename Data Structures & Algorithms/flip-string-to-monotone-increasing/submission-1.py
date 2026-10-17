class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0 # store how many ones i see
        flips = 0 # to find minimum flip i need to to all 1 or all 0 

        for char in s:
            if char == "1":
                ones += 1

            else:
                flips = min(flips + 1, ones)

        return flips
        
        
        
        
        
         # if the string valid the minimum flips will remain zero thats why i didnt need isvalid function

