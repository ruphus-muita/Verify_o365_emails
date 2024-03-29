import re

def is_valid_o365_email(email):
    # Regular expression for validating email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.onmicrosoft\.com$"
    return bool(re.match(pattern, email))

# Test email addresses
email1 = "rmuita@appliedprinciples.co.ke"
email2 = "lkiiru@appliedprinciples.co.ke"

print(is_valid_o365_email(email1)) # True
print(is_valid_o365_email(email2)) # False
