from typing import List



class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i: int, j: int, group: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1 or visited[i][j]:
                return 0
            visited[i][j] = True
            component_sizes[group] += 1
            cell_to_group[i * n + j] = group
            size = 1
            for di, dj in directions:
                size += dfs(i + di, j + dj, group)
            return size

        visited = [[False] * n for _ in range(n)]
        component_sizes = {}
        cell_to_group = {}
        group = 0
        max_size = 0

        # First pass: Identify all connected components
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    component_sizes[group] = 0
                    size = dfs(i, j, group)
                    max_size = max(max_size, size)
                    group += 1

        # Second pass: Try flipping 0's to 1's
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_groups=set()
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            neighbor_groups.add(cell_to_group[ni * n + nj])
                    
                    size = 1  # Include the cell we're changing to 1
                    for g in neighbor_groups:
                        size += component_sizes[g]
                    
                    max_size = max(max_size, size)

        return max_size

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]




#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends