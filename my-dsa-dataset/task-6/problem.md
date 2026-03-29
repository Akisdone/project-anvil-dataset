# Task: Two Sum
Implement a function `two_sum(arr: list, target: int) -> list` that finds two numbers in an array that add up to a target sum.

## Requirements

1. Return a list of TWO indices [i, j] where arr[i] + arr[j] = target
2. i must be less than j (i < j)
3. You cannot use the same element twice
4. Return indices in ascending order
5. If no solution exists, return an empty list []

## Constraints

- Array can have 0 to 1000 elements
- Array contains integers (positive and negative)
- Target is an integer
- If multiple solutions exist, return ANY valid pair

## Examples

Input: arr = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: arr[0] + arr[1] = 2 + 7 = 9

Input: arr = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: arr[1] + arr[2] = 2 + 4 = 6

Input: arr = [3, 3], target = 6
Output: [0, 1]
Explanation: arr[0] + arr[1] = 3 + 3 = 6

Input: arr = [1, 2, 3], target = 7
Output: []
Explanation: No pair sums to 7

Input: arr = [], target = 5
Output: []
Explanation: Empty array has no pairs

Input: arr = [5], target = 10
Output: []
Explanation: Need at least 2 elements