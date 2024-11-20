class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low, high = max(weights), sum(weights)
        ans = 0
        
        def calculate_days(capacity):
            days_needed = 1
            batch=0    
            
            for w in weights:
                if batch + w > capacity :
                    days_needed += 1
                    batch = w
                else:
                    batch += w
                    
            return days_needed
    
        while (low <= high):            
            mid = (low + high) // 2
            
            if calculate_days(mid) <= days:
                ans = mid
                high = mid - 1
          
            else:
                low = mid + 1
                
        return ans
                
            
            
            