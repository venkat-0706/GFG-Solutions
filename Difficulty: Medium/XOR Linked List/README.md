<h2><a href="https://www.geeksforgeeks.org/problems/xor-linked-list/1">XOR Linked List</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">An ordinary Doubly Linked List requires space for two address fields to store the addresses of previous and next nodes. A memory-efficient version of the Doubly Linked List can be created using only one space for the address field with every node. This memory-efficient Doubly Linked List is called XOR Linked List or Memory Efficient as the list uses bit-wise XOR operation to save space for one address.<br><br>Given a stream of data of size <strong>N </strong>for the linked list, your task is to complete the function <strong>insert()&nbsp;</strong>and <strong>getList(). </strong>The <strong>insert()</strong> function pushes (or inserts at the beginning) the given data in the linked list and the </span><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; font-size: 18px;">getList()</strong><span style="font-size: 18px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">&nbsp;&nbsp;function returns the linked list as a list.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> </span></p>
<ol>
<li><span style="font-size: 18px;">A utility function XOR() takes two Node pointers to get the bit-wise XOR of the two Node pointers. Use this function to get the XOR of the two pointers.</span></li>
<li><span style="font-size: 18px;">The driver code prints the returned list twice, once forward and once backwards.</span></li>
</ol>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>LinkedList: 9&lt;-&gt;5&lt;-&gt;4&lt;-&gt;7&lt;-&gt;3&lt;-&gt;10<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700562/Web/Other/blobid0_1720967479.png" width="400" height="60"><br><strong>Output:
</strong>10 3 7 4 5 9
9 5 4 7 3 10</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>LinkedList: 58&lt;-&gt;96&lt;-&gt;31<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700562/Web/Other/blobid0_1721214940.png" width="230" height="65"><br><strong>Output:
</strong>31 96 58
58 96 31</span>
</pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= number of nodes, data of nodes &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>GE</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>doubly-linked-list</code>&nbsp;<code>Linked List</code>&nbsp;<code>Data Structures</code>&nbsp;