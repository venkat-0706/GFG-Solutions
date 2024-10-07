

class Solution:
    def minPoints(self, m, n, points):
        j = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        j[m-1][n]=1
        j[m][n-1]=1
        for i in range(m-1,-1,-1):
            for k in range(n-1,-1,-1):
                j[i][k]=max(1,(min(j[i+1][k],j[i][k+1])-points[i][k]))
        
        return j[0][0]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends