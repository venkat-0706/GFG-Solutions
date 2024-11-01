#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        ans=[]
        arr.sort()
        i=0
        n=len(arr)
        while len(ans)<n:
            if i%2==0:
                ans.append(arr.pop(0))
            else:
                ans.append(arr.pop())
            i+=1
        ans.append(ans[0])
        final=0
        for i in range(n):
            final+=abs(ans[i]-ans[i+1])
        return final 


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends