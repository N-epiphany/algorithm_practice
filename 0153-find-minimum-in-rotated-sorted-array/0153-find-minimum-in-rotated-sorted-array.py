class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        low = 0
        high = len(nums) - 1
        
        if nums[high] > nums[0]:
            return nums[0]
            
        while low <= high:
            mid = (low + high) // 2
            
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
        return nums[0] 