<h2><a href="https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/0">Smallest window in a string containing all the characters of another string</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings <strong>s</strong> and <strong>p</strong>. Find the smallest window in the string <strong>s</strong> consisting of all the characters(<strong>including duplicates</strong>) of the string <strong>p</strong>.&nbsp;</span>&nbsp;<span style="font-size: 18px;">Return "<strong>-1</strong>" in case there is no such window present.&nbsp;In case there are multiple such windows of same length, return the one with the <strong>least starting index</strong>.<br><strong>Note</strong> : All characters are in Lowercase alphabets.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: s</strong> = "timetopractice", p = "toc"
<strong>Output: </strong>toprac<strong>
Explanation: "</strong>toprac" is the smallest
substring in which "toc" can be found.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "zoomlazapzo", p = "oza"
<strong>Output: </strong>apzo<strong>
Explanation: </strong><strong>"</strong>apzo" is the smallest 
substring in which "oza" can be found.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(|s|)<br><strong>Expected Auxiliary Space: </strong>O(n), n = len(p)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:&nbsp;</strong><br>1 ≤ |s|, |p| ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Google</code>&nbsp;<code>Streamoid Technologies</code>&nbsp;<code>Media.net</code>&nbsp;<code>Atlassian</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>Hash</code>&nbsp;<code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;