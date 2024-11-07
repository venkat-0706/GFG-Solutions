<h2><a href="https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170645/1">Minimum repeat to make substring</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given two strings <strong>s1 </strong>and<strong> s2. </strong>Return a minimum number of times s1 has to be repeated such that s2 is a substring of it. If <strong>s2</strong> can never be a substring then return <strong>-1</strong>.</span></p>
<p><span style="font-size: 14pt;">Note: Both the strings contain only lowercase letters.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "ww", s2 = "www"
<strong>Output: </strong>2
<strong>Explanation: </strong>Repeating s1 two times (wwww), s2 is a substring of it.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "abcd", s2 = "cdabcdab" <br><strong>Output: </strong>3 <br><strong>Explanation: </strong>Repeating s1 three times (abcdabcdabcd), s2 is a substring of it. s2 is not a substring of s2 when it is repeated less than 3 times.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "ab", s2 = "cab"
<strong>Output: </strong>-1
<strong>Explanation: </strong>No matter how many times we repeat s1, we can't get a string such that s2 is a substring of it.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ |s1|, |s2| ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Searching</code>&nbsp;<code>Strings</code>&nbsp;<code>Pattern Searching</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;