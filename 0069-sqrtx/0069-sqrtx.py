class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans=0
        while (low<=high):
            mid =(low+high)//2
            sqr = mid*mid
            
            if sqr == x:
                return mid

            if sqr<x:
                ans=mid
                low=mid+1
            if sqr > x:
                high = mid-1  
                
        return ans
        