class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i+1:] :
                j=nums[i+1:].index(rem)+i+1
                break
        return [i,j]