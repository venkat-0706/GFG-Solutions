<h2><a href="https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&sortBy=submissions">Minimize the Heights II</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong>&nbsp;denoting heights of <strong>N</strong> towers and a positive integer <strong>K. </strong></span></p>
<p><span style="font-size: 18px;">For <strong>each </strong>tower, you must perform <strong>exactly one</strong> of the following operations <strong>exactly once</strong>.</span></p>
<ul>
<li><span style="font-size: 18px;"><strong>Increase </strong>the height of the tower by <strong>K</strong></span></li>
<li><span style="font-size: 18px;"><strong>Decrease </strong>the height of the tower by <strong>K</strong></span></li>
</ul>
<p><span style="font-size: 18px;">Find out the <strong>minimum </strong>possible difference between the height&nbsp;of the shortest and tallest towers after you have modified each tower.</span></p>
<p><span style="font-size: 18px;">You can find a slight modification of the problem&nbsp;<a href="https://practice.geeksforgeeks.org/problems/minimize-the-heights-i/1/">here</a>.<br><strong>Note:</strong> It is <strong>compulsory </strong>to increase or decrease the height by K for each tower. <strong>After</strong> the operation, the resultant array should <strong>not</strong> contain any <strong>negative integers</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>k = 2, arr[] = {1, 5, 8, 10}
<strong>Output: </strong>5
<strong>Explanation: </strong>The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>k = 3, arr[] = {3, 9, 12, 16, 20}
<strong>Output: </strong>11
<strong>Explanation: </strong>The array can be modified as </span><span style="font-size: 18px;">{3+k, 9+k, 12-k, 16-k, 20-k} -&gt; {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11.&nbsp;
</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n*logn)<br><strong>Expected Auxiliary Space:</strong> O(n)<br></span></p>
<p><span style="font-size: 18px;"><strong>Constraints</strong><br>1 ≤ k ≤ 10<sup>7</sup><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>7</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Greedy</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;