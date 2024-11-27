<h2><a href="https://www.geeksforgeeks.org/problems/implement-atoi/1">Implement Atoi</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.</span></p>
<p><strong><span style="font-size: 18px;">Cases for atoi() conversion:</span></strong></p>
<ol>
<li><span style="font-size: 18px;">Skip any leading whitespaces.</span></li>
<li><span style="font-size: 18px;">Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.</span></li>
<li><span style="font-size: 18px;">Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.</span></li>
<li><span style="font-size: 18px;">If the integer is greater than 2<sup>31</sup> – 1, then return 2<sup>31</sup> – 1 and if the integer is smaller than -2<sup>31</sup>, then return -2<sup>31</sup>.</span></li>
</ol>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">s = "-123"
</span><strong style="font-size: 18px;">Output: -</strong><span style="font-size: 18px;">123<br></span><strong style="font-size: 18px;">Explanation: </strong><span style="font-size: 18px;">It is possible to convert -123 into an integer so we returned in the form of an integer<br></span></span></pre>
<pre><span style="font-size: 18px;"><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">s = "<span style="color: #273239; font-family: Nunito, sans-serif; font-style: italic; letter-spacing: 0.162px; text-wrap-mode: wrap; background-color: #f9f9f9;">  -</span>"
</span><strong style="font-size: 18px;">Output: </strong><span style="font-size: 18px;">0<br></span><strong style="font-size: 18px;">Explanation: </strong><span style="font-size: 18px;"><span style="font-size: 18px;">No digits are present, therefore the returned answer is 0.<br></span></span></span></span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = " 1231231231311133"
<strong>Output: </strong>2147483647<br><strong>Explanation: </strong>T</span><span style="font-size: 18px;">he converted number will be greater than 2<sup>31</sup> – 1, therefore print 2<sup>31</sup> – 1 = 2147483647.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "-999999999999"
<strong>Output: -</strong>2147483648<br><strong>Explanation: </strong></span><span style="font-size: 14pt;">The converted number is smaller than -2<sup>31</sup>, therefore print -2<sup>31</sup> = -2147483648.</span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">s = "  -0012gfg4"
</span><strong style="font-size: 18px;">Output: </strong><span style="font-size: 18px;">-12</span><strong style="font-size: 18px;">
Explanation: </strong></span><span style="font-size: 18px;">Nothing is read after -12 as a non-digit character ‘g’ was encountered.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ |s| ≤ 15</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Morgan Stanley</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Payu</code>&nbsp;<code>Adobe</code>&nbsp;<code>Code Brew</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Design-Pattern</code>&nbsp;<code>Data Structures</code>&nbsp;