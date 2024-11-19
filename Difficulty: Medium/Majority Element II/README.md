<h2><a href="https://www.geeksforgeeks.org/problems/majority-vote/1">Majority Element II</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given an array of integer <strong>arr[]</strong> where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array.&nbsp;</span></p>
<p><strong><span style="font-size: 18px;">Note:</span></strong><span style="font-size: 18px;"> The answer should be returned in an increasing format.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [</span><span style="font-size: 18px;">2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
<strong>Output: </strong>[5, 6]
<strong>Explanation: </strong>5 and 6 occur more n/3 times.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 2, 3, 4, 5]
<strong>Output: </strong>[]<br><strong>Explanation: </strong>no candidate occur more than n/3 times.</span></pre>
<p><strong><span style="font-size: 18px;">Constraint:</span></strong><br><span style="font-size: 18px;">1 &lt;= arr.size() &lt;= 10<sup>6</sup><br>0 &lt;= arr[i] &lt;= 10<sup>9</sup></span></p></div>