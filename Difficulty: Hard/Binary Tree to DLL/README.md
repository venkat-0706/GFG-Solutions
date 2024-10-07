<h2><a href="https://www.geeksforgeeks.org/problems/binary-tree-to-dll/0">Binary Tree to DLL</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 12pt;">Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. The <strong>order of nodes</strong> in DLL must be the same as the order of the given Binary Tree. The first node of <strong>Inorder traversal</strong> (leftmost node in BT) must be the head node of the DLL.<br><br><strong>Note: </strong>h&nbsp;is the tree's height, and this space is used implicitly for the recursion stack.</span></p>
<p><span style="font-size: 12pt;"><img style="height: 234px; width: 375px;" src="http://www.geeksforgeeks.org/wp-content/uploads/TreeToList.png" alt="TreeToList"></span></p>
<p><span style="font-size: 12pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 12pt;"><strong>Input:
</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1
 &nbsp;&nbsp;&nbsp;/&nbsp; \
 &nbsp;&nbsp;3&nbsp;&nbsp;&nbsp; 2
<strong>Output:<br></strong>3 1 2 
2 1 3<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700144/Web/Other/blobid0_1723093893.png" width="375" height="244"><strong>
Explanation:</strong> DLL would be 3&lt;=&gt;1&lt;=&gt;2</span></pre>
<pre><span style="font-size: 12pt;"><strong>Input:
</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10
 &nbsp;&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp; \
     20&nbsp;&nbsp; 30
 &nbsp; /&nbsp;&nbsp; \
 &nbsp;40&nbsp;&nbsp; 60
<strong>Output:
</strong>40 20 60 10 30 
30 10 60 20 40<br><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700144/Web/Other/blobid1_1723093972.png" width="374" height="271"><br>Explanation: </strong> DLL would be 40&lt;=&gt;20&lt;=&gt;60&lt;=&gt;10&lt;=&gt;30.</span></pre>
<p><span style="font-size: 12pt;"><strong>Expected Time Complexity:&nbsp;</strong>O(no. of nodes)<br><strong>Expected Space&nbsp;</strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Complexity</strong><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">: </strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">O(height of the tree)</span></span></p>
<p><span style="font-size: 12pt;"><strong>Constraints:</strong><br>1 ≤ Number of nodes ≤ 10<sup>5</sup><br>0 ≤ Data of a node ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Morgan Stanley</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>Goldman Sachs</code>&nbsp;<code>Salesforce</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Linked List</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;