#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        lis = []
        seen = set()
        for num in arr:
            if num not in seen:
                lis.append(num)
                seen.add(num)
        return lis
            
        # code here 
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends