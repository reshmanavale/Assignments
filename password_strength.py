import re

def check_password_strength(password):
    """
    Checks if the given password meets the required criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    # Check minimum length
    if len(password) < 8:
        return False
    
    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all checks pass, the password is strong
    return True

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")

    if check_password_strength(password):
        print("Your password is strong!")
    else:
        print("Your password does not meet the required criteria:")
        print(" - At least 8 characters long")
        print(" - Contains both uppercase and lowercase letters")
        print(" - Contains at least one digit (0-9)")
        print(" - Contains at least one special character (e.g., !, @, #, $)")

if __name__ == "__main__":
    main()
