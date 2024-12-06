class Solution:
    #User function Template for python3
    def merge_sort(self, arr, inversion_count):
        if len(arr) == 1 or len(arr) == 0:
            return arr
        n = len(arr)
        mid = n // 2
        left = self.merge_sort(arr[0:mid], inversion_count)
        right = self.merge_sort(arr[mid:], inversion_count)
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                inversion_count[0] = inversion_count[0] + len(left) - i
                res.append(right[j])
                j += 1
        if i < len(left):
            while i < len(left):
                res.append(left[i])
                i += 1

        if j < len(right):
            while j < len(right):
                res.append(right[j])
                j += 1
        return res
    def inversionCount(self, arr):
        inversion_count = [0]
        res = self.merge_sort(arr, inversion_count)
        return inversion_count[0]

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
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends