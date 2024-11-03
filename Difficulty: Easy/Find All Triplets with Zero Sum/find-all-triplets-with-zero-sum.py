#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def findTriplets(self, arr):
        # Your code here
        d={}
        n=len(arr)
        temp=0
        for i in range(0,n):
            for j in range(i+1,n):
                temp=arr[i]+arr[j]
                if(temp in d):
                    d[temp].append([i,j])
                else:
                    d[temp]=[[i,j]]
        tpt=[]
        vis={}
        ans=[]
        for i in range(n):
            temp=-arr[i]
            if(temp in d):
                for a,b in d[temp]:
                    tpt=sorted([i,a,b])
                    if(i!=a and i!=b and (tuple(tpt) not in vis)):
                        ans.append(tpt)
                        vis[tuple(tpt)]=1
        return ans

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends