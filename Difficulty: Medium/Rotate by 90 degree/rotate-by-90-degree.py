#User function Template for python3
def rotate(matrix): 
    #code here
    
    n = len(matrix)
    def transpose(m):
        n = len(m)
        for i in range(n):
            for j in range(i+1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]
    
    transpose(matrix)
    for r in range(n):
        matrix[r].reverse()
    return matrix

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends