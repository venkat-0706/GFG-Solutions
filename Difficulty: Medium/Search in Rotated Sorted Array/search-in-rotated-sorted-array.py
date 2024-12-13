#User function Template for python3

class Solution:
    def search(self,arr,key):
        n = len(arr)
        for i in range(n):
            if key not in arr:
                return -1
            return arr.index(key)
        # Complete this function


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends