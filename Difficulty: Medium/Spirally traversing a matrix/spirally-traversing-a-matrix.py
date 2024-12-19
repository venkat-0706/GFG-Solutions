class Solution:
    def spirallyTraverse(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        k = 2 * min(m, n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, -1
        res = []
        for d in range(k):
            for i in range(n):
                x += dx[d % 4]
                y += dy[d % 4]
                res.append(matrix[x][y])
            m, n = n, m - 1
        return res



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends