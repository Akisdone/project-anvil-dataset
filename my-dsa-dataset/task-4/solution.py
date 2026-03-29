import re

def check_password_strength(password):
    length = len(password)
    if length < 6:
        return "Weak"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    met_count = sum([has_upper, has_lower, has_digit, has_special])
    if length >= 12 and met_count == 4:
        return "Strong"
    if (length >= 8 and met_count >= 2) or (length >= 6 and met_count == 4):
        return "Medium"
    return "Weak"