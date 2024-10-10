<h2><a href="https://www.geeksforgeeks.org/problems/max-distance-between-same-elements/1">Max distance between same elements</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 20px;">Given an array <strong>arr[]</strong> with repeated elements, the task is to find the maximum distance between two occurrences of an element.</span></p>
<p><span style="font-size: 14pt;">Note:&nbsp;<span style="background-color: #ffffff; color: #222222; font-family: Arial, Helvetica, sans-serif;">You may assume that every input array has repetitions.</span></span></p>
<p><span style="font-size: 20px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 20px;"><strong>Input: </strong></span><span style="font-size: 20px;">arr = [1, 1, 2, 2, 2, 1]</span>
<span style="font-size: 20px;"><strong>Output: </strong>5</span>
<span style="font-size: 20px;"><strong>Explanation: </strong>distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.</span></pre>
<pre><span style="font-size: 20px;"><strong>Input: </strong>arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]</span>
<span style="font-size: 20px;"><strong>Output: </strong>10</span>
<span style="font-size: 20px;"><strong>Explanation: </strong></span><span style="font-size: 20px;">maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity </strong>:&nbsp; O(n)<br><strong>Expected Auxilliary Space </strong>: O(n)</span></p>
<p><span style="font-size: 20px;"><strong>Constraints:<br></strong></span><span style="font-size: 20px;">1 &lt;= arr.size() &lt;= 10<sup>6</sup><br>1 &lt;= arr[i] &lt;= 10<sup>9</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;<code>Data Structures</code>&nbsp;