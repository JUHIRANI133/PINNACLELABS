import re

def analyze_password(password):
    feedback = []
    score = 0

    if len(password) >= 12: 
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider increasing password length to 12+ characters.")
    else:
        feedback.append("Password too short! Use at least 8-12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc).")

    weak_passwords = ["password", "123456", "qwerty", "admin", "abc123"]
    if password.lower() in weak_passwords:
        score = 0
        feedback.append("Password is too common! Avoid dictionary words or popular passwords.")

    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def check_breach(password):
    try:
        with open("breached_passwords.txt", "r") as file:
            breached = file.read().splitlines()
        return password in breached
    except FileNotFoundError:
        return False  
