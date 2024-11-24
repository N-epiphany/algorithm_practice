class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#          0 1 2 3 4 5 6
#         [1,2,3,4,5,6,7] 
#         [5,6,7,1,2,3,4]
#         n = 6
#         i = 0
#         k = 3
        
#         temp = nums[i+k]
#         nums[i+k] = nums [i]
#         nums[i] = temp
        n = len(nums)
        k = k % n 
    
        def reverse(start, end):
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
            
        reverse(0, n-1)      
        reverse(0, k-1)      
        reverse(k, n-1)     
        