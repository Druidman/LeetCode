class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        number = 0
        i=0
        while i<len(s)-1:
            if s[i]+s[i+1] in nums:
                number += nums[s[i]+s[i+1]]
                i+=2
            else:
                number += nums[s[i]]
                i+=1
        if i == len(s)-1:
            
        
            number += nums[s[i]]
            
       
        return number




sol = Solution()

print(sol.romanToInt("IV"))