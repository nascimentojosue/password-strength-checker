import re

def check_password_strength(password):
    # Initialize a score variable
    score = 0
    feedback = []
    
    # Length criteria
    if len(password) < 6:
        feedback.append("Password is too short; aim for at least 8 characters.")
    elif 6 <= len(password) < 8:
        score += 1
        feedback.append("Password length is okay but could be longer for added security.")
    elif len(password) >= 8:
        score += 2
        feedback.append("Good length for a strong password.")
    
    # Character diversity criteria
    if re.search(r'[a-z]', password):  # Lowercase
        score += 1
    else:
        feedback.append("Add lowercase letters for more security.")
        
    if re.search(r'[A-Z]', password):  # Uppercase
        score += 1
    else:
        feedback.append("Add uppercase letters for more security.")
        
    if re.search(r'[0-9]', password):  # Digits
        score += 1
    else:
        feedback.append("Add numbers for more security.")
        
    if re.search(r'[\W_]', password):  # Special characters
        score += 2
        feedback.append("Adding special characters makes the password stronger.")
    else:
        feedback.append("Consider adding special characters (e.g., !, @, #, $).")
    
    # Common patterns check
    common_patterns = ["password", "1234", "qwerty", "abcd"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common patterns like 'password' or '1234'.")
        score -= 1
    
    # Provide final strength message based on score
    if score <= 2:
        strength = "Very Weak"
    elif 3 <= score <= 4:
        strength = "Weak"
    elif 5 <= score <= 6:
        strength = "Moderate"
    elif 7 <= score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength, feedback
