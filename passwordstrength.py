import re

def check_password_strength(password):
    strength_points = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("Password should be at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one special character (!@#$ etc).")

    # Final verdict
    print("\n🔎 Strength Check Result:")
    if strength_points == 5:
        print("✅ Strong password!")
    elif 3 <= strength_points < 5:
        print("⚠️ Medium strength password.")
    else:
        print("❌ Weak password.")

    # Suggestions
    if suggestions:
        print("\n🛠️ Suggestions to improve your password:")
        for s in suggestions:
            print(f"- {s}")

def main():
    print("=== 🛡️ Password Strength Checker ===")
    password = input("Enter your password to check: ").strip()
    check_password_strength(password)

if __name__ == "__main__":
    main()
