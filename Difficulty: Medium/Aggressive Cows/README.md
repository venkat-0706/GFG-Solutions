<h2><a href="https://www.geeksforgeeks.org/problems/aggressive-cows/1">Aggressive Cows</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given an array with unique elements of stalls[],<strong> </strong>which denote the position of a <strong>stall</strong>. You are also given an integer <strong>k</strong> which denotes the number of aggressive cows. Your task is to assign <strong>stalls </strong>to<strong> k </strong>cows such that the <strong>minimum distance </strong>between any two of them is the<strong> maximum </strong>possible.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>stalls[] = [1, 2, 4, 8, 9], k = 3
<strong>Output: </strong>3
<strong>Explanation: </strong>The first cow can be placed at stalls[0], <br>the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>stalls[] = [10, 1, 2, 7, 5], k = 3
<strong>Output: </strong>4
<strong>Explanation: </strong>The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>stalls[] = [2, 12, 11, 3, 26, 7], k = 5
<strong>Output: </strong>1
<strong>Explanation: </strong>Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong></span><br><span style="font-size: 14pt;">2 &lt;= stalls.size() &lt;= 10<sup>6</sup><br></span><span style="font-size: 18.6667px;">0 &lt;= stalls[i] &lt;= 10<sup>8</sup></span><br><span style="font-size: 14pt;">1 &lt;= k &lt;= </span><span style="font-size: 18.6667px;">stalls.size()</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search</code>&nbsp;<code>Algorithms</code>&nbsp;