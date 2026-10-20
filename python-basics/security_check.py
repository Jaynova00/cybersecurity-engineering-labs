def check_password_length(password):
    """Check whether a password meets a minimum length."""
    if len(password) < 12:
        return "Weak: password must be at least 12 characters."

    return "Length requirement met."


password = input("Enter a test password: ")
result = check_password_length(password)

print(result)
