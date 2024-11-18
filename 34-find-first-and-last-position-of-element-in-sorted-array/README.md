<h2><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array">Find First and Last Position of Element in Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find the starting and ending position of a given target value in a sorted array.
        
        Approach:
        - Use binary search (via bisect) to find the leftmost and rightmost positions
        - bisect_left finds the insertion point for target to maintain sorted order
        - bisect_right finds the insertion point after the last occurrence
        
        Time Complexity: O(log n) - Binary search is used twice
        Space Complexity: O(1) - Only constant extra space is used
        
        Args:
            nums: A sorted array of integers
            target: The target value to search for
            
        Returns:
            List[int]: [start_position, end_position], returns [-1, -1] if target not found
        
        Example:
            >>> sol = Solution()
            >>> sol.searchRange([5,7,7,8,8,10], 8)
            [3, 4]
            >>> sol.searchRange([5,7,7,8,8,10], 6)
            [-1, -1]
        """
        if not nums: 
            return [-1, -1]
            
        lower = bisect_left(nums, target)
        
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
            
        upper = bisect_right(nums, target) - 1
        return [lower, upper]
