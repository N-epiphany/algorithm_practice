#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # basic approach is to sort and then select the second last element , but
        # since we are not sorting and it will be complexity nlogn
        # 12, 35, 1, 10, 34, 1
        # without sorting
        largest = arr[0]    
        sec_largest = -1
        
        if len(arr) == 1:
            return sec_largest
        for i in range(len(arr)):
            # print(i)
            if arr[i] > largest :
                # print(largest," ",sec_largest)
                sec_largest=largest
                largest= arr[i]
                # print("after exchange :",largest," ",sec_largest)
            if arr[i] < largest and arr[i]> sec_largest:
                sec_largest = arr[i]
                # print ("new sec",sec_largest)
            
        return sec_largest        
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends