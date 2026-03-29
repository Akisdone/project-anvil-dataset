def is_valid(s: str) -> bool:
    if not s:
        return True
    
    stack = []
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0


