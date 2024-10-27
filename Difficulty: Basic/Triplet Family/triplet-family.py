class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        for i in range(n):
            for j in range(n):
                res = arr[i] + arr[j]
                if i!=j and res in arr and res!=arr[i] and res!=arr[j]:
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends