class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        for i in range(n):
            nums1.pop(-1)
    
        nums1+= nums2

        nums1.sort()





sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0],m = 3,n=3,nums2 = [2,5,6])

