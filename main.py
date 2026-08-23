from password_checker import check_password_strength, suggest_password, estimate_crack_time

print("🔐 Password strength checker")

password = input("Enter your password: ")

strength = check_password_strength(password)
print("Password strength:", strength)

crack_time = estimate_crack_time(password)
print("Estimated crack time:", crack_time)

if "Weak" in strength:
    print("Suggested strong password:", suggest_password())
