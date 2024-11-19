<h2><a href="https://leetcode.com/problems/valid-perfect-square">Valid Perfect Square</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>Given a positive integer num, return <code>true</code> if num is a perfect square or <code>false</code> otherwise.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.</p>

<p>You must not use any built-in library function, such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> num = 16
<strong>Output:</strong> true
<strong>Explanation:</strong> 4 * 4 = 16, so return true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> num = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> No integer n exists such that n * n = 14.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 <= num <= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Approach:</strong></p>
<p>The solution uses binary search to efficiently find if a perfect square root exists:</p>
<ul>
    <li>Search space is from 1 to num</li>
    <li>For each mid point, calculate mid * mid</li>
    <li>If mid * mid equals num, we found a perfect square</li>
    <li>If mid * mid > num, search in lower half</li>
    <li>If mid * mid < num, search in upper half</li>
</ul>

<p><strong>Why Binary Search?</strong></p>
<ul>
    <li>Instead of checking every number from 1 to num (O(n))</li>
    <li>Binary search reduces time complexity to O(log n)</li>
    <li>Especially efficient for large numbers</li>
</ul>

<p><strong>Complexity Analysis:</strong></p>
<ul>
    <li>Time Complexity: <code>O(log n)</code> - Binary search cuts search space in half each time</li>
    <li>Space Complexity: <code>O(1)</code> - Only using constant extra space</li>
</ul>

<p><strong>Implementation:</strong></p>

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1
                
        return False
```

<p><strong>Example Walk-through:</strong></p>
<pre>
num = 16:
1. low = 1, high = 16, mid = 8
   8 * 8 = 64 > 16
   high = 7

2. low = 1, high = 7, mid = 4
   4 * 4 = 16 == 16
   return True

num = 14:
1. low = 1, high = 14, mid = 7
   7 * 7 = 49 > 14
   high = 6

2. low = 1, high = 6, mid = 3
   3 * 3 = 9 < 14
   low = 4

3. low = 4, high = 6, mid = 5
   5 * 5 = 25 > 14
   high = 4

4. low = 4, high = 4, mid = 4
   4 * 4 = 16 > 14
   high = 3

5. low = 4, high = 3
   low > high, return False
</pre>

<p><strong>Note:</strong></p>
<p>The variable <code>flag</code> in the original code is unnecessary since we return True immediately when we find a perfect square.</p>
