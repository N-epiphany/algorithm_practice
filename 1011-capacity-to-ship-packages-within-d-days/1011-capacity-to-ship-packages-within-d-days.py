class Solution:
    
    def total_days(self,weights,max_w):
        days=1
        batch=0
        
        for i in weights:
            if batch + i > max_w :
                days +=1
                batch = i
            else:
                batch +=i
                
        return days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        ans=0
        
        while (low<= high):            
            mid = (low+high)//2
            total_days = self.total_days(weights,mid)
            if total_days <= days:
                ans= mid
                high=mid-1
          
            else:
                low=mid+1
        return ans
                
            
            
            