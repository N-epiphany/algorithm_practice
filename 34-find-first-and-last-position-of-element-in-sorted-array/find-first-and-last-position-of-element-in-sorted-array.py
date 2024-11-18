from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return [-1, -1]
            
        lower = bisect_left(nums, target)
        
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
            
        upper = bisect_right(nums, target) - 1
        return [lower, upper]