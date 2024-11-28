#User function Template for python3

class Solution:
    def rotate(self, arr):
        k = arr[-1]
        n=len(arr)
        for i in range(n):
            arr[i], k = k,arr[i]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends