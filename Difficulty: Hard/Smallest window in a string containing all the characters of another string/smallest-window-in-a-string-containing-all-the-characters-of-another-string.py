#User function Template for python3


class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        
        s1 = [0] * 256
        p1 = [0] * 256
        min_length = float('inf')
        
        for ch in p:
            p1[ord(ch) - ord('a')] += 1
        
        j = 0
        start_idx = -1
        count = 0
        
        for i in range(len(s)):
            s1[ord(s[i]) - ord('a')] += 1
            
            if p1[ord(s[i]) - ord('a')] != 0 and s1[ord(s[i]) - ord('a')] <= p1[ord(s[i]) - ord('a')]:
                count += 1
            
            if count == len(p):
                while p1[ord(s[j]) - ord('a')] == 0 or s1[ord(s[j]) - ord('a')] > p1[ord(s[j]) - ord('a')]:
                    if s1[ord(s[j]) - ord('a')] > p1[ord(s[j]) - ord('a')]:
                        s1[ord(s[j]) - ord('a')] -= 1
                    j += 1
                
                length = i - j + 1
                if length < min_length:
                    min_length = length
                    start_idx = j
        
        if start_idx == -1:
            return "-1"
        
        return s[start_idx:start_idx + min_length]


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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends