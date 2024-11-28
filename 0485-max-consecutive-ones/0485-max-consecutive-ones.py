class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one=0
        curr=0
        for i in nums:           
            if i == 0:
                if curr > max_one :
                    max_one=curr
                curr=0
            else:            
                curr+=1
                if curr > max_one :
                    max_one=curr
        return max_one