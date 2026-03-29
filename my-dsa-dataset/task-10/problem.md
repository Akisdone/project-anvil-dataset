# Task: Find Rotation Point in Sorted Rotated Array

Implement a function `find_rotation_point(arr: list) -> int` that finds the rotation point (minimum element) in a rotated sorted array.

## What is a Rotated Sorted Array?

A sorted array that has been rotated at some pivot point.

Examples:
- Original: [1, 2, 3, 4, 5, 6, 7]
- Rotated at index 3: [4, 5, 6, 7, 1, 2, 3]
- The rotation point is index 4 (where value 1 is)

## Requirements

1. Return the INDEX of the minimum element (rotation point)
2. Array is originally sorted in ascending order, then rotated
3. All elements are unique
4. Array length >= 1
5. Must be efficient (O(log n) preferred, not O(n))

## Examples

Input: [4, 5, 6, 7, 1, 2, 3]
Output: 4
(Index 4 contains 1, which is the minimum)

Input: [1, 2, 3, 4, 5, 6, 7]
Output: 0
(Not rotated, minimum at index 0)

Input: [3, 4, 5, 1, 2]
Output: 3
(Index 3 contains 1, the minimum)

Input: [5, 1, 2, 3, 4]
Output: 1
(Index 1 contains 1, the minimum)

Input: [1]
Output: 0
(Single element, minimum at index 0)

Input: [2, 1]
Output: 1
(Index 1 contains 1, the minimum)