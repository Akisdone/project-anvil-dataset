def validate_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    if " " in email:
        return False
    username, domain = email.split("@")
    if not username:
        return False
    if not domain:
        return False
    if "." not in domain:
        return False
    
    return True