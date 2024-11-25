//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Sorting {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            int arr[] = new int[str.length];
            for (int i = 0; i < str.length; i++) arr[i] = Integer.parseInt(str[i]);
            System.out.println(new Solution().circularSubarraySum(arr));
            // System.out.println("~");
        }
    }
}
// } Driver Code Ends

class Solution {
    public int circularSubarraySum(int arr[]) {
        int prefixSum = 0;
        int maxSum = Integer.MIN_VALUE;
        
        int sum = 0;
        for (int num : arr) {
            sum += num;
            prefixSum += num;
            maxSum = Math.max(maxSum, sum);
            sum = Math.max(sum, 0);
        }

        int currSum = 0;
        for (int num : arr) {
            currSum += num;
            currSum = Math.min(0, currSum);
            maxSum = Math.max(maxSum, prefixSum - currSum);
        }
        
        return maxSum;
    }
}
