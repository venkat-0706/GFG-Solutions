#User function Template for python3

class Solution:
    def minIncrements(self, arr):
        arr.sort()
        m , count = -1 , 0
        for e in arr:
            m = max(m+1 , e)
            count +=  m - e
        return count
                    
        
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends