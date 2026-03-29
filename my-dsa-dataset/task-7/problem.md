# Task: Valid Parentheses

Implement a function `is_valid(s: str) -> bool` that checks if a string of parentheses is valid.

## Requirements

1. Return `True` if parentheses are balanced and in correct order
2. Return `False` if they are not
3. Handle three types of brackets: (), {}, []
4. Empty string is considered valid

## Rules

- Every opening bracket must have a corresponding closing bracket
- Closing bracket must match the type of the most recent opening bracket
- Brackets must be closed in the correct order

## Examples

✓ Valid:
- "" (empty)
- "()" 
- "()[]{}"
- "{[()]}"
- "((()))"

✗ Invalid:
- "(" (unclosed)
- ")" (no opening)
- "([)]" (wrong order)
- "{[}]" (mismatched)
- "([)]" (interleaved)