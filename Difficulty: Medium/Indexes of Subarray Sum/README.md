<h2><a href="https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions">Indexes of Subarray Sum</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an unsorted array <strong>arr </strong>of size <strong>n</strong> that contains only non negative integers, find a sub-array (</span><span style="font-size: 18px;">continuous elements)</span><span style="font-size: 18px;"> that has sum equal to <strong>s</strong>. You mainly need to return the left and right indexes(<strong>1-based indexing</strong>) of that subarray.</span></p>
<p><span style="font-size: 18px;">In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. </span><span style="font-size: 18px;">If no such subarray exists return an array consisting of element <strong>-1</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1,2,3,7,5], </span><span style="font-size: 18px;">n = 5, s = 12</span><span style="font-size: 18px;">
<strong>Output: </strong>2 4<strong>
Explanation: </strong>The sum of elements from 2nd to 4th position is 12.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1,2,3,4,5,6,7,8,9,10], </span><span style="font-size: 18px;">n = 10, s = 15,</span><span style="font-size: 18px;">
<strong>Output: </strong>1 5<strong>
Explanation: </strong>The sum of elements from 1st to 5th position is 15.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [7,2,1], </span><span style="font-size: 18px;">n = 3, s = 2</span><span style="font-size: 18px;">
<strong>Output: </strong>2 2<strong>
Explanation: </strong>The sum of elements from 2nd to 2nd position is 2.<br></span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [5,3,4], </span><span style="font-size: 18px;">n = 3, s = 2</span><span style="font-size: 18px;">
<strong>Output: </strong>-1<strong>
Explanation: </strong>There is no subarray with sum 2</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(n)<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<p><span style="font-size: 18px;">0 &lt;= arr[i] </span><span style="font-size: 18px;">&lt;= 10<sup>9</sup></span><br><span style="font-size: 18px;">1 &lt;= n &lt;= 10<sup>5</sup></span><br><span style="font-size: 18px;">0 &lt;= s</span><span style="font-size: 18px;"> &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Facebook</code>&nbsp;<code>Google</code>&nbsp;<code>Visa</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Algorithms</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>prefix-sum</code>&nbsp;<code>Searching</code>&nbsp;<code>sliding-window</code>&nbsp;