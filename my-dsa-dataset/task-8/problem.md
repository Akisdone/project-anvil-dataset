# Task: Merge Two Sorted Arrays

Implement a function `merge_sorted_arrays(arr1: list, arr2: list) -> list` that merges two sorted arrays into one sorted array.

## Requirements

1. Both input arrays are already sorted in ascending order
2. Return a single merged array that is also sorted
3. The merged array should contain all elements from both arrays
4. Return an empty list if both inputs are empty
5. Handle arrays of different lengths

## Constraints

- Array length can be 0 to 1000
- Elements are integers (positive, negative, or zero)
- Both arrays are guaranteed to be sorted

## Examples

Input: [1, 3, 5], [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: [1, 2, 3], [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: [], [1, 2, 3]
Output: [1, 2, 3]

Input: [], []
Output: []

Input: [1, 5, 9], [2, 3, 8, 13]
Output: [1, 2, 3, 5, 8, 9, 13]

Input: [-5, -1, 0], [-3, 2, 4]
Output: [-5, -3, -1, 0, 2, 4]