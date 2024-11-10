class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for element in strs[1:]:
                if not element.startswith(letter,i):
                    return prefix
            prefix += letter
        return prefix


       
  

sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))

