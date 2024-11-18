class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = bisect_left(nums,target)   
        if lower == len(nums):
            upper = bisect_right(nums,target)
            return upper
        else :
            return lower
    
