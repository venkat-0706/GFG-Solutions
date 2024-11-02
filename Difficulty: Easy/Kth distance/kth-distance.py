#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        n = len(arr)
        for i in range(n-1):
            if(arr[i] in arr[i+1:i+k+1]):
                return True
        return False
        # your code


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends