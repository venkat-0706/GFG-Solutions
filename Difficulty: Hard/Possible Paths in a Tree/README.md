<h2><a href="https://www.geeksforgeeks.org/problems/possible-paths--141628/0">Possible Paths in a Tree</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a <strong>weighted</strong> tree with <strong>n</strong> nodes and (<strong>n-1</strong>) edges. You are given <strong>q</strong> <strong>queries</strong>. Each query contains a number <strong>x</strong>. For each query, find the number of paths in which the maximum edge weight is less than or equal to <strong>x</strong>. </span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> Path from A to B and B to A are considered to be the same.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>n = 3
edges {start, end, weight} = {{1, 2, 1}, {2, 3, 4}}</span>
<span style="font-size: 18px;">q = 1
queries[] = {3}
<strong>Output:</strong> <br>1
<strong>Explanation:</strong>
Query 1: Path from 1 to 2</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>n = 7
</span><span style="font-size: 18px;">edges {start, end, weight} = {{1, 2, 3}, {2, 3, 1}, {2, 4, 9}, {3, 6, 7}, {3, 5, 8}, {5, 7, 4}}
</span><span style="font-size: 18px;">q = 3
queries[] = {1, 3, 5}
<strong>Output:</strong> <br>1 3 4
<strong>Explanation:</strong> </span>
<span style="font-size: 18px;">Query 1: Path from 2 to 3</span>
<span style="font-size: 18px;">Query 2: Path from 1 to 2, 1 to 3, and 2 to 3</span>
<span style="font-size: 18px;">Query 3: Path from 1 to 2, 1 to 3, 2 to 3, and 5 to 7</span>
</pre>
<p><span style="font-size: 18px;"><strong>Your Task: &nbsp;</strong><br>You don't need to read input or print anything. Complete the function <strong>maximumWeight()</strong>which takes integers <strong>n,</strong>&nbsp;list of&nbsp;<strong>edges</strong> where each edge is given by {start,end,weight}, an integer <strong>q </strong>and a list of q <strong>queries</strong> as input parameters and returns a list of integers denoting the number of possible paths for each query.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(nlogn + qlogn)<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>2 ≤ n ≤ 10<sup>4<br></sup>1 ≤ q ≤ 10<sup>4</sup><sup><br></sup></span><span style="font-size: 18px;">1 </span><span style="font-size: 18px;">≤ edges[i][0], edges[i][1]&nbsp;</span><span style="font-size: 18px;">≤ n<br></span><span style="font-size: 18px;">edges[i][0] != edges[i][1]<br></span><span style="font-size: 18px;">0 </span><span style="font-size: 18px;">≤ </span><span style="font-size: 18px;">edges[i][2] </span><span style="font-size: 18px;">≤ 10<sup>5</sup><br>0&nbsp;≤&nbsp;queries[i] ≤ 10<sup>5</sup><br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;<code>union-find</code>&nbsp;