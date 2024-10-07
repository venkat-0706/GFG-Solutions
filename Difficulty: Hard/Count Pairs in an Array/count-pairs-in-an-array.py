#User function Template for python3

class Solution:    
    def countPairs(self,arr, n): 
        import bisect
        tempArr = []
        
        for i, num in enumerate(arr):
            tempArr.append(i*num)

        newArr = []
        count= 0
        for num in tempArr:
            ind = bisect.bisect(newArr, num)
            count += (len(newArr) - ind)
            newArr.insert(ind, num)
            
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends