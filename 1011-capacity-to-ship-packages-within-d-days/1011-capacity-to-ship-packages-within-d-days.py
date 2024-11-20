class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low, high = max(weights), sum(weights)
        ans = 0
        
        def calculate_days(capacity):
            days_needed = 1
            batch=0        
            for weight in weights:
                if batch + weight > capacity :
                    days_needed +=1
                    batch = weight
                else:
                    batch +=weight
            return days_needed
    
        while (low <= high):            
            mid = (low + high) // 2
            total_days = calculate_days(mid)
            
            if total_days <= days:
                ans = mid
                high = mid - 1
          
            else:
                low = mid+1
        return ans
                
            
            
            