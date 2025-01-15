import re
def validate_password(password):
    if len(password) < 6 or len(password)> 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False

    return True

input_password = input("Enter a password: ")
if validate_password(input_password):
    print("Password is valid.")
else:
    print("Password is invalid.")

