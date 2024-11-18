<h2><a href="https://leetcode.com/problems/search-insert-position">Search Insert Position</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
    <li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
    <li><code>nums</code> contains distinct values sorted in ascending order.</li>
    <li><code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Approach:</strong></p>
<p>The solution utilizes Python's <code>bisect_left</code> function from the bisect module, which efficiently handles all possible cases in a single operation:</p>
<ul>
    <li>When target is found in the array → returns its exact index</li>
    <li>When target is between elements → returns the index where it should be inserted</li>
    <li>When target is larger than all elements → returns len(nums)</li>
    <li>When target is smaller than all elements → returns 0</li>
</ul>

<p><strong>Complexity Analysis:</strong></p>
<ul>
    <li>Time Complexity: <code>O(log n)</code> - Uses binary search internally</li>
    <li>Space Complexity: <code>O(1)</code> - Only constant extra space is used</li>
</ul>

<p><strong>Implementation:</strong></p>

```python
from bisect import bisect_left
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
```

<p><strong>Example Cases Breakdown:</strong></p>
<pre>
nums = [1,3,5,6]

Case 1: target = 5 (Element exists)
- bisect_left returns 2
- 5 is at index 2 ✓

Case 2: target = 2 (Element doesn't exist)
- bisect_left returns 1
- 2 should be inserted between 1 and 3 ✓

Case 3: target = 7 (Larger than all elements)
- bisect_left returns 4 (len(nums))
- 7 should be inserted at the end ✓

Case 4: target = 0 (Smaller than all elements)
- bisect_left returns 0
- 0 should be inserted at the beginning ✓
</pre>
