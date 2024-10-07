<h2><a href="https://www.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/0">Construct Binary Tree from Parent Array</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array<strong> parent</strong> that is used to represent a tree. The array indices (0-based indexing) are the values of the tree nodes and <strong>parent[i] </strong>denotes the parent node of a particular node. The parent of the root node would always be <strong>-1,</strong> as there is no parent for the root. Construct the standard linked representation of Binary Tree from this array representation and </span><span style="font-size: 18px;"><strong>return the root</strong> node of the constructed tree</span><span style="font-size: 18px;">.</span></p>
<p><strong><span style="font-size: 18px;">Note: </span></strong><span style="font-size: 18px;">If two elements have the same parent, the one that appears first in the array will be the left child and the other is the right child. You don't need to print anything, the driver code will print the level order traversal of the returned root node to verify the output.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">parent[] = [-1, 0, 0, 1, 1, 3,5]
<strong>Output: </strong>0 1 2 3 4 5 6<strong>
Explanation: </strong>the tree generated
will have a structure like 
&nbsp;       &nbsp; 0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  /&nbsp;&nbsp; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  1&nbsp;&nbsp;&nbsp;&nbsp; 2
&nbsp;&nbsp;&nbsp;&nbsp;  / \
&nbsp;&nbsp;&nbsp;  3&nbsp;&nbsp; 4
&nbsp;&nbsp;  /
&nbsp;  5
 /
6</span></pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">parent[] = [2, 0, -1]
<strong>Output: </strong>2 0 1<strong>
Explanation: </strong>the tree generated will
have a structure like
&nbsp; &nbsp; &nbsp; &nbsp;  &nbsp;&nbsp; &nbsp;2
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;/&nbsp;&nbsp; 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  0&nbsp;  &nbsp;  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /&nbsp;&nbsp; 
&nbsp; &nbsp; &nbsp; &nbsp;  1   &nbsp; </span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(n)<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ parent.size() ≤ 10<sup>3</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Snapdeal</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;