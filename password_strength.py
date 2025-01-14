import re

def check_password_strength(password):
    """Evaluate the strength of a password."""
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

  
    errors = {
        "Too short": length_error,
        "Missing digit": digit_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing symbol": symbol_error,
    }

    strength = "Strong" if not any(errors.values()) else "Weak"
    return strength, [key for key, value in errors.items() if value]


password = input("Enter a password to evaluate: ")
strength, issues = check_password_strength(password)

print(f"Password Strength: {strength}")
if issues:
    print("Issues:")
    for issue in issues:
        print(f"- {issue}")
