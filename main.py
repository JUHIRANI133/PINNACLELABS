from password_analyzer import analyze_password, check_breach

print(" Password Strength Analyzer")
print("="*35)

password = input("Enter a password to analyze: ")


if check_breach(password):
    print("\n This password has appeared in a data breach! Avoid using it.")

strength, suggestions = analyze_password(password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("\nSuggestions to Improve:")
    for tip in suggestions:
        print(f" - {tip}")
else:
    print(" Your password looks secure!") 
