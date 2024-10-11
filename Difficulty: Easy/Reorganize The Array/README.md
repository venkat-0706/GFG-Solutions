<h2><a href="https://www.geeksforgeeks.org/problems/reorganize-the-array4810/1">Reorganize The Array</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of elements <strong>arr[]</strong> with indices ranging from <strong>0</strong> to <strong>arr.size()</strong> - 1, your task is to write a program that rearranges the elements of the array such that <strong>arr[i]</strong> = <strong>i</strong>. If an element <strong>i</strong> is not present in the array, <strong>-1</strong> should be placed at the corresponding index.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
<strong>Output:</strong> [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
<strong>Explanation: </strong>Here We can see there are 10 elements. So, the sorted array will look like [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] but in our array we are not having 0, 5, 7 and 8. So, at there places we will be printing -1 and otherplaces will be having elements.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [2, 0, 1]
<strong>Output:</strong> [0, 1, 2]
<strong>Explanation: </strong>Here We can see all the elements are present so no -1 is returned in array.
</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n).<br><strong>Expected Auxiliary Space:</strong> O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>0 ≤ arr.size() ≤ 10<sup>5</sup><br>-1 ≤ arr[i] ≤ arr.size()-1<br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;