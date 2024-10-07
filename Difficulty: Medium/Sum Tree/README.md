<h2><a href="https://www.geeksforgeeks.org/problems/sum-tree/0">Sum Tree</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><div class="entry-content">
<p><span style="font-size: 18px;">Given a Binary Tree. Check for the <strong>Sum Tree</strong> for every node except the leaf node. Return true if it is a Sum Tree otherwise, return false.</span></p>
<blockquote>
<p><span style="font-size: 18px;"><span style="color: #273239; font-family: Nunito, sans-serif; letter-spacing: 0.162px; background-color: #ffffff;">A <strong>SumTree</strong> is a Binary Tree where the value of a node is equal to the sum of the nodes present in its<strong> left</strong> subtree and <strong>right </strong>subtree. </span></span><span style="font-size: 18px;">An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be <strong>0</strong>. A leaf node is also considered a Sum Tree.</span></p>
</blockquote>
<p><strong><span style="font-size: 18px;">Examples :</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
    3
  /   \    
 1     2</span>
<span style="font-size: 18px;"><strong>Output:</strong> true</span>
<span style="font-size: 18px;"><strong>Explanation: </strong>The sum of left subtree and right subtree is 1 + 2 = 3, which is the value of the root node. Therefore,the given binary tree is a sum tree.</span>
</pre>
<pre><strong><span style="font-size: 18px;">Input:</span></strong>
<span style="font-size: 18px;">          10
        /    \
      20      30
    /   \ 
   10    10</span>
<span style="font-size: 18px;"><strong>Output: </strong>false</span>
<span style="font-size: 18px;"><strong>Explanation: </strong>The given tree is not a sum tree. For the root node, sum of elements in left subtree is 40 and sum of elements in right subtree is 30. Root element = 10 which is not equal to 30+40.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(n)<br><strong>Expected Auxiliary Space:</strong> O(Height of the Tree</span><span style="font-size: 18px;">)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>2 ≤ number of nodes ≤ 10<sup>5<br></sup></span><span style="font-size: 18px;">1 ≤ node value ≤ 10</span><sup>5</sup></p>
</div></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>D-E-Shaw</code>&nbsp;<code>Goldman Sachs</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;