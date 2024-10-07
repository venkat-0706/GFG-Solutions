<h2><a href="https://www.geeksforgeeks.org/problems/burning-tree/0">Burning Tree</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a binary tree and a&nbsp;<strong>node data</strong> called <strong>target</strong>. Find the minimum time required to burn the complete binary tree if the target is set on fire.&nbsp;It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.<br><strong>Note:</strong> The tree contains unique values.</span></p>
<p><br><strong><span style="font-size: 18px;">Examples :&nbsp;</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:      </strong>
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10</span>
<span style="font-size: 18px;">Target Node = 8</span>
<span style="font-size: 18px;"><strong>Output:</strong> 7</span>
<span style="font-size: 18px;"><strong>Explanation:</strong> If leaf with the value 8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong>      
          1
        /   \
      2      3
    /  \      \
   4    5      7
  /    / 
 8    10</span>
<span style="font-size: 18px;">Target Node = 10</span>
<span style="font-size: 18px;"><strong>Output:</strong> 5</span>
</pre>
<p><br><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(number of nodes)<br><strong>Expected Auxiliary Space: </strong>O(height of tree)</span></p>
<p><br><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤&nbsp;</span><span style="font-size: 18px;">number of nodes</span><span style="font-size: 18px;">&nbsp;≤ 10</span><sup>5</sup></p>
<p><span style="font-size: 18px;">1 ≤&nbsp;</span><span style="font-size: 18px;">values of nodes</span><span style="font-size: 18px;">&nbsp;≤ 10</span><sup>5</sup></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>BFS</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;