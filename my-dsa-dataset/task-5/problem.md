# Task: Find All Duplicates in an Array

Implement a function `find_duplicates(arr: list) -> list` that finds all duplicate elements in an array.

## Requirements

1. Return a list of all elements that appear MORE than once
2. Each duplicate element should appear ONCE in the result (no repeats)
3. Return elements in ascending order
4. Empty array returns empty list

## Constraints

- Array contains integers from 1 to n (where n is array length)
- Array length can be 0 to 1000
- Do not use extra space (optimal solution uses O(1) space)

## Examples

Input: [1, 2, 2, 3, 3, 3]
Output: [2, 3]

Input: [1, 1, 1, 1]
Output: [1]

Input: [1, 2, 3, 4, 5]
Output: []

Input: [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]

Input: []
Output: []