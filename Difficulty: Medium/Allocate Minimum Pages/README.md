<h2><a href="https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1">Allocate Minimum Pages</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given an array <code>arr[]</code> of integers, where each element <code>arr[i]</code> represents the number of pages in the ith book. You also have an integer <code>k</code> representing the number of students. The task is to allocate books to each student such that:</span></p>
<ul>
<li><span style="font-size: 14pt;">Each student receives <strong>atleast</strong> one book.</span></li>
<li><span style="font-size: 14pt;">Each student is assigned a contiguous sequence of books.</span></li>
<li><span style="font-size: 14pt;">No book is assigned to more than one student.</span></li>
</ul>
<p><span style="font-size: 14pt;">The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.</span></p>
<p><span style="font-size: 18px;"><strong>Note</strong>: Return <strong>-1</strong> if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [12, 34, 67, 90], k = 2
<strong>Output: </strong>113
<strong>Explanation: </strong>Allocation can be done in following ways:
[12] and [34, 67, 90] Maximum Pages = 191
[12, 34] and [67, 90] Maximum Pages = 157
[12, 34, 67] and [90] Maximum Pages = 113.
Therefore, the minimum of these cases is 113, which is selected as the output.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [15, 17, 20], k = 5
<strong>Output: </strong>-1
<strong>Explanation: </strong>Allocation can not be done.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [22, 23, 67], k = 1
<strong>Output: </strong>112</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;=&nbsp; arr.size() &lt;= 10<sup>6</sup><br>1 &lt;= arr[i] &lt;= 10<sup>3<br></sup></span><span style="font-size: 18px;">1 &lt;= k &lt;= 10<sup>3&nbsp;</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Infosys</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Google</code>&nbsp;<code>Codenation</code>&nbsp;<code>Uber</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Divide and Conquer</code>&nbsp;<code>Algorithms</code>&nbsp;