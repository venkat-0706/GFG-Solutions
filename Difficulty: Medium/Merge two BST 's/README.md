<h2><a href="https://www.geeksforgeeks.org/problems/merge-two-bst-s/0">Merge two BST 's</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two BSTs, return elements of merged BSTs in <strong>sorted </strong>form.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>BST1:
       5
&nbsp;    /   \
&nbsp;   3     6
&nbsp;  / \
&nbsp; 2   4  
BST2:<strong>
&nbsp;       </strong>2
&nbsp;     /   \
&nbsp;    1     3
&nbsp;           \
&nbsp;            7
&nbsp;           /
&nbsp;          6
<strong>Output: </strong>1 2 2 3 3 4 5 6 6 7<strong>
Explanation: </strong>After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>BST1:<strong>
&nbsp;      </strong>12
&nbsp;    /   
&nbsp;   9
&nbsp;  / \ &nbsp;  
&nbsp; 6   11
BST2:<strong>
&nbsp;     </strong>8
&nbsp;   /  \
&nbsp;  5    10
&nbsp; /
&nbsp;2
<strong>Output: </strong>2 5 6 8 9 10 11 12<strong>
Explanation: </strong>After merging and sorting the two BST we get 2 5 6 8 9 10 11 12.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O((m+n)*log(m+n))<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(Height of BST1 + Height of BST2 + m + n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ Number of Nodes, value of nodes ≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;