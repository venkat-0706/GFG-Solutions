#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        n = len(arr)
        # Step 2: Initialize the difference between the highest and lowest before any modifications
        result = arr[n-1] - arr[0]
        
        # Step 3: Traverse the array and adjust the heights
        for i in range(1, n):
            if arr[i] >= k:  # Ensure no negative heights
                # Calculate the possible new minimum and maximum heights
                max_height = max(arr[i-1] + k, arr[n-1] - k)
                min_height = min(arr[0] + k, arr[i] - k)
                # Update the result with the minimum possible difference
                result = min(result, max_height - min_height)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends