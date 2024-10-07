<h2><a href="https://www.geeksforgeeks.org/problems/maximum-connected-group/0">Maximum Connected group</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given a square&nbsp;binary grid. A grid is considered binary if every value in the grid is either&nbsp;<strong>1 or 0.&nbsp;</strong></span><span style="font-size: 18px;">You can change&nbsp;<strong>at most one</strong>&nbsp;cell in the grid from&nbsp;<strong>0 to 1</strong>.&nbsp;</span><span style="font-size: 18px;">You need to find the largest group of connected&nbsp;&nbsp;<strong>1's</strong>.&nbsp;</span><span style="font-size: 18px;">Two cells are said to be connected if both are&nbsp;<strong>adjacent</strong>(top, bottom, left, right)&nbsp;to each other and both have the same value.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong></span><span style="font-size: 18px;">grid = [1, 1]
             [0, 1]
<strong>Output</strong>: 4
<strong>Explanation</strong>: By changing cell (2,1), we can obtain a connected group of 4 1's
[1, 1]
[<strong>1,</strong> 1]</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: grid = [1, 0, 1]<br></span><span style="font-size: 18px;">             [1, 0, 1]
             [1, 0, 1]
<strong>Output</strong>: 7
<strong>Explanation</strong>: By changing cell (3,2), we can obtain a connected group of 7 1's
[1, 0, 1]<br>[1, 0, 1]
[1, <strong>1,</strong> 1]</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity</strong>: O(n<sup>2</sup>)<br><strong>Expected Auxiliary Space</strong>: O(</span><span style="font-size: 18px;">n</span><sup>2</sup><span style="font-size: 18px;">)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints</strong>:<br>1 &lt;= size of the grid&lt;= 500<br>0 &lt;= grid[i][j] &lt;= 1<br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>BFS</code>&nbsp;<code>Graph</code>&nbsp;<code>DFS</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;