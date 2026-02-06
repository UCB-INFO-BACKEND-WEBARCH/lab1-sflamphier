"""
Password Security Tool - INFO 153B/253B Lab 1

Analyze password strength and generate secure passwords.

"""

import string
import random

# Common weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley"
]


# ============================================
# TODO 1: Password Strength Checker
# ============================================

def check_password_strength(password):
    """
    Analyze password and return strength score.
    
    Scoring:
    - 8+ characters: 20 points
    - 12+ characters: 30 points (instead of 20)
    - Has number: 20 points
    - Has uppercase: 20 points
    - Has lowercase: 20 points
    - Has special char (!@#$%): 20 points
    - Not in common list: 10 points
    
    Returns:
        dict with keys: "password", "score", "strength", "feedback"
        
    Strength levels:
    - 0-39: "Weak"
    - 40-69: "Medium"
    - 70-100: "Strong"
    
    Example:
        >>> result = check_password_strength("Hello123!")
        >>> result["score"]
        90
        >>> result["strength"]
        "Strong"
    
    Hint: Use .isdigit(), .isupper(), .islower() and string.punctuation
    """
    # TODO: Implement this function
    
    score = 0 # Total password strength score (0-100)
    feedback = [] # So we can see what we are doing wrong and how to improve
    
    # 12+ characters: 30 points (instead of 20)
    if len(password) >= 12:
        score += 30
    # 8+ characters: 20 points
    elif len(password) >= 8:
        score += 20
    
    # Has number: 20 points
    if any(c.isdigit() for c in password):
        score += 20
    else:
        feedback.append("Add numbers")
    
    # Has uppercase: 20 points
    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase letters")
    
    # Has lowercase: 20 points
    if any(c.islower() for c in password):
        score += 20
    else:
        feedback.append("Add lowercase letters")
    
    # Has special char (!@#$%): 20 points
    special_chars = "!@#$%^&*()-+"
    if any(c in special_chars for c in password):
        score += 20
    else:
        feedback.append("Add special characters --> !@#$%^&*()-+ ")
    
    # Not in common list: 10 points
    if password not in COMMON_PASSWORDS:
        score += 10
    else:
        feedback.append("Don't use common passwords")
    
    # Password strength level
    strength = "Weak"
    if score >= 70:
        strength = "Strong"
    elif score >= 40:
        strength = "Medium"
    
    return {
        "password": password,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# ============================================
# TODO 2: Password Generator
# ============================================

def generate_password(length=12, use_special=True):
    """
    Generate a random secure password.
    
    Requirements:
    - Include uppercase, lowercase, and numbers
    - Include special characters if use_special=True
    - Minimum length: 8
    
    Args:
        length: Password length (default 12)
        use_special: Include special characters (default True)
    
    Returns:
        str: Generated password
    
    Example:
        >>> pwd = generate_password(10, True)
        >>> len(pwd)
        10
    
    Hint: Use string.ascii_uppercase, string.ascii_lowercase, 
          string.digits, and random.choice()
    """

    # Ensure minimum of 8
    length = max(length, 8)

    # Build characters
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    special_chars = "!@#$%^&*()-+"
    if use_special:
        characters += special_chars

    # Pasword must have one uppercase, one lowercase and one digit
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]

    # Include special characters if use_special=True
    if use_special:
        password_chars.append(random.choice(special_chars))

    # Fill the rest of the password with random choices
    while len(password_chars) < length:
        password_chars.append(random.choice(characters))
    # Shuffle to avoid predictable ordering
    random.shuffle(password_chars)
    return ''.join(password_chars)

# ============================================
# Simple Testing
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PASSWORD SECURITY TOOL - Quick Test")
    print("=" * 60 + "\n")
    
    # Check if functions are implemented
    try:
        # Test TODO 1
        result = check_password_strength("TestPassword123!")
        
        if result is None:
            print("❌ TODO 1 not implemented yet (returned None)")
            print("\nImplement check_password_strength() and try again.\n")
            exit()
        
        if not isinstance(result, dict):
            print("❌ TODO 1 should return a dictionary")
            exit()
        
        required_keys = ["password", "score", "strength", "feedback"]
        missing_keys = [key for key in required_keys if key not in result]
        
        if missing_keys:
            print(f"❌ TODO 1 missing keys in return dict: {missing_keys}")
            exit()
        
        print("✓ TODO 1 implemented - returns correct structure")
        print(f"  Example: '{result['password']}' → {result['strength']} ({result['score']}/100)")
        
        # Test TODO 2
        pwd = generate_password(12, True)
        
        if pwd is None:
            print("\n❌ TODO 2 not implemented yet (returned None)")
            print("\nImplement generate_password() and try again.\n")
            exit()
        
        if not isinstance(pwd, str):
            print("\n❌ TODO 2 should return a string")
            exit()
        
        print(f"\n✓ TODO 2 implemented - generates passwords")
        print(f"  Example: '{pwd}' (length: {len(pwd)})")
        
        # Success!
        print("\n" + "=" * 60)
        print("✅ Both functions implemented!")
        print("=" * 60)
        print("\nRun the full test suite to verify correctness:")
        print("  python test_password_tool.py")
        print()
        
    except AttributeError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure both functions are defined.\n")
    except Exception as e:
        print(f"❌ Error running functions: {e}")
        print("\nCheck your implementation and try again.\n")
