
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        freq = [0] * n
        result = []
        for num in arr:
            freq[num] += 1
        for i in range(n):
            if freq[i] > 1:
                result.append(i)
        return result if result else [-1]


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends