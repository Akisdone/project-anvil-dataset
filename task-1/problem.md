# Task: Validate Email Format

Implement a function `validate_email(email: str) -> bool` that validates an email address.

## Requirements

1. Returns `True` if the email is valid
2. Returns `False` if the email is invalid

## Validation Rules

- Must contain exactly one `@` symbol
- Must have at least one character before `@` (username)
- Must have at least one character after `@` (domain)
- Domain must contain at least one dot (e.g., `example.com`)
- Spaces are NOT allowed anywhere in the email

## Examples

✓ Valid:
- `user@example.com`
- `john.doe@company.co.uk`
- `a@b.c`
- `test123@mail.org`

✗ Invalid:
- `user@` (no domain)
- `@example.com` (no username)
- `user@@example.com` (two @ symbols)
- `user@example` (no dot in domain)
- `user @example.com` (space not allowed)
- `userexample.com` (no @ symbol)