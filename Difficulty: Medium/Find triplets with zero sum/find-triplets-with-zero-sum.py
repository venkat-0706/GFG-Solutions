class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        count = 0
        arr.sort()

        for i in range(n-2):
            if (i > 0 and arr[i] == arr[i-1]):
                continue
            
            j, k = i+1, n-1
            while (j < k):
                sum_of_3 = arr[i] + arr[j] + arr[k]
                if sum_of_3 == 0:
                    count += 1
                    j += 1
                    k -= 1
                elif sum_of_3 < 0:
                    j += 1
                else:
                    k -= 1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        if (Solution().findTriplets(a, n)):
            print(1)
        else:
            print(0)

# } Driver Code Ends