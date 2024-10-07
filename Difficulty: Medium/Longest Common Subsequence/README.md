<h2><a href="https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1?page=4&sortBy=submissions">Longest Common Subsequence</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings <strong>str1</strong> &amp; <strong>str 2</strong> of length <strong>n</strong> &amp; <strong>m</strong> respectively, return the length of their <strong>longest common subsequence. </strong>If there is no common subsequence then, <strong>return 0</strong>.&nbsp;</span></p>
<blockquote>
<p><em><span style="box-sizing: border-box; margin: 0px; padding: 0px; border: 0px; font-size: 18px; vertical-align: baseline; color: #273239; font-family: Nunito, sans-serif; letter-spacing: 0.162px; text-align: justify; background-color: #f9f9f9;"><span style="color: #273239; font-family: Nunito, sans-serif;"><span style="font-size: 18px; letter-spacing: 0.162px;">A subsequence is a sequence that can be derived from the given string by deleting some or no elements without changing the order of the remaining elements. </span></span><span style="color: #273239; font-family: Nunito, sans-serif;"><span style="font-size: 18px; letter-spacing: 0.162px;">For example, "abe" is a subsequence of "abcde".</span></span></span></em></p>
</blockquote>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 6, str1 = ABCDGH and m = 6, str2 = AEDFHR
<strong>Output: </strong>3<strong>
Explanation: </strong>LCS for input strings “ABCDGH” and “AEDFHR” is “ADH” of length 3.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 3, str1 = ABC and m = 2, str2 = AC
<strong>Output: </strong>2<strong>
Explanation: </strong>LCS of "ABC" and "AC" is "AC" of length 2.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 3:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 4, str1 = XYZW and m = 4, str2 = XYWZ
<strong>Output: 3</strong><strong>
Explanation: </strong>There are two common subsequences of length 3 “XYZ”, and”XYW”, and no common subsequence. of length more than 3.<br></span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You do not need to read input or print anything. Complete the function <strong>lcs()</strong> which takes the two strings and their lengths as input parameters and returns the length of the Longest Common Subsequence.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity</strong>: O(n*m)<br><strong>Expected Auxiliary Space</strong>: O(n*m)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1&lt;= n, m &lt;=10<sup>3<br></sup></span><span style="font-size: 18px;"><sup><span style="font-size: 15px;">str1 and str2 are in uppercase alphabet</span></sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Paytm</code>&nbsp;<code>VMWare</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Citrix</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Algorithms</code>&nbsp;