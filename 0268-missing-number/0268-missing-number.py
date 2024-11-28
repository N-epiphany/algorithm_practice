class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i in nums:
        #         continue
        #     else :
        #         return i
        
        n= len(nums)
        s=(n*(n+1))//2
        return s-sum(nums)