# Task: Password Strength Checker

Implement a function `check_password_strength(password: str) -> str` that evaluates a string and returns "Weak", "Medium", or "Strong".

### Scoring Rules:
1. **Strong**: 
   - At least 12 characters long.
   - Contains at least one uppercase letter, one lowercase letter, one number, and one special character (e.g., !@#$%^&*).
2. **Medium**: 
   - At least 8 characters long.
   - Contains at least two of the following: uppercase, lowercase, numbers, or special characters.
3. **Weak**: 
   - Anything that doesn't meet Medium or Strong requirements.
   - Any password shorter than 6 characters is always "Weak".

### Example:
- `check_password_strength("P@ssw0rd2026!")` -> "Strong"
- `check_password_strength("password123")` -> "Medium"
- `check_password_strength("123")` -> "Weak"