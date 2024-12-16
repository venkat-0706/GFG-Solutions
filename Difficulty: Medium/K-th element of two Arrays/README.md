<h2><a href="https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1">K-th element of two Arrays</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two sorted arrays <strong>a[] </strong>and <strong>b[]</strong> and an element <strong>k</strong>, the task is to find the element that would be at the <strong>k<sup>th</sup></strong> position of the combined sorted array.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
<strong>Output: </strong>6
<strong>Explanation: </strong>The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
<strong>Output: </strong>256
<strong>Explanation: </strong>Combined sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">1 &lt;= a.size(), b.size() &lt;= 10<sup>6</sup></span></li>
<li><span style="font-size: 18px;">1 &lt;= k &lt;= a.size() + b.size()</span></li>
<li><span style="font-size: 18px;">0 &lt;= a[i], b[i] &lt; 10<sup>8</sup><br></span></li>
</ul></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Divide and Conquer</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;<code>Binary Search</code>&nbsp;