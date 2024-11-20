class Solution:
    def total_time(self,piles , k):
        total_time = 0
        for i in piles:
            total_time += ceil(i/k)            
        return total_time
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = -1
        low = 1
        high = max(piles)
        while (low <= high) :           
            mid = (low + high) // 2 #this is our prospective k 
            ans = self.total_time(piles,mid)
            if (ans <= h):
                k=mid
                high=mid-1
            elif ans >h:
                low=mid+1
                
        return k
            
            
