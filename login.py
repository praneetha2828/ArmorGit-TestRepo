def validate_email(email):
    if "@" not in email:
        return False

    if "." not in email:
        return False

    return True


def login(email, password):
    if not validate_email(email):
        return "Invalid email"

    return "Login successful"
