<h2><a href="https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-with-distinct-elements/1">Union of Two Sorted Arrays with Distinct Elements</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two&nbsp;<strong>sorted</strong>&nbsp;arrays&nbsp;<strong>a[]</strong>&nbsp;and&nbsp;<strong>b[]</strong>, where each array contains <strong>distinct</strong>&nbsp;elements , the task is to return the elements in the&nbsp;<strong>union</strong>&nbsp;of the two arrays in&nbsp;<strong>sorted</strong>&nbsp;order.</span></p>
<blockquote><span style="font-size: 18px;">Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.</span></blockquote>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]</span><br><span style="font-size: 18px;"><strong>Output</strong>: 1 2 3 4 5 6 7</span><br><span style="font-size: 18px;"><strong>Explanation</strong>: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: a[] = [2, 3, 4, 5], b[] = [1, 2, 3, 4]
<strong>Output</strong>: 1 2 3 4 5
<strong>Explanation</strong>: Distinct elements including both the arrays are: 1 2 3 4 5.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: a[] = [1], b[] = [2]
<strong>Output</strong>: 1 2
<strong>Explanation</strong>: Distinct elements including both the arrays are: 1 2.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1&nbsp; &lt;=&nbsp; a.size(), b.size()&nbsp; &lt;=&nbsp; 10<sup>5</sup><br>-10<sup>9</sup>&nbsp; &lt;=&nbsp; a[i] , b[i]&nbsp; &lt;=&nbsp; 10<sup>9</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;