#User function Template for python3

class Solution:
      def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        arr.reverse()
        d %= n
        arr[:n-d] = reversed(arr[:n-d])
        arr[n-d:] = reversed(arr[n-d:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends