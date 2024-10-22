<h2><a href="https://www.geeksforgeeks.org/problems/sub-arrays-with-equal-number-of-occurences3901/1">Sub-arrays with equal number of occurences</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[] </strong>and two integers say, <strong>x&nbsp;</strong>and <strong>y</strong>, find the number of sub-arrays in which the number of occurrences of <strong>x</strong> is equal to the number of occurrences of <strong>y</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 1] , x= 1 , y = 2
<strong>Output:</strong> 2
<strong>Explanation: </strong>The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1, 2], x and y have same occurrence(1).
2) [2, 1], x and y have same occurrence(1).<br></span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 1] , x = 4 , y = 6
<strong>Output:</strong> 6
<strong>Explanation: </strong>The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1], x and y have same occurrence(0).
2) [2], x and y have same occurrence(0).
3) [1], x and y have same occurrence(0).
4) [1, 2], x and y have same occurrence(0).
5) [2, 1], x and y have same occurrence(0).
6) [1, 2, 1], x and y have same occurrence(0).<br></span></pre>
<pre><strong>Input: </strong>arr[] = [1, 2, 1] , x= 1 , y = 4
<strong>Output:</strong> 1
<strong>Explanation: </strong>The possible sub-array have same equal number of occurrences of x and y is: [2], x and y have same occurrence(0)</pre>
<p><span style="font-size: 18px;"><strong>Constraints:&nbsp;</strong><br>1 &lt;= arr.size() &lt;= 10<sup>6</sup><br>1 &lt;= arr[i], x, y&lt;=10<sup>6</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>STL</code>&nbsp;<code>Data Structures</code>&nbsp;