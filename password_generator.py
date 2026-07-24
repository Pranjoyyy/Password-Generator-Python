import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:

    # ---------- Password Length ----------
    while True:
        try:
            length = int(input("\nEnter password length (8-50): "))

            if length < 8:
                print("❌ Password must be at least 8 characters long.\n")

            elif length > 50:
                print("❌ Password cannot be longer than 50 characters.\n")

            else:
                break

        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

    # ---------- Include Numbers ----------
    while True:
        include_numbers = input("Include numbers? (Y/N): ").strip().lower()

        if include_numbers in ["y", "yes"]:
            include_numbers = True
            break

        elif include_numbers in ["n", "no"]:
            include_numbers = False
            break

        else:
            print("❌ Invalid option! Please type Y, N, Yes, or No.\n")

    # ---------- Include Symbols ----------
    while True:
        include_symbols = input("Include symbols? (Y/N): ").strip().lower()

        if include_symbols in ["y", "yes"]:
            include_symbols = True
            break

        elif include_symbols in ["n", "no"]:
            include_symbols = False
            break

        else:
            print("❌ Invalid option! Please type Y, N, Yes, or No.\n")

    # ---------- Characters ----------
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    # ---------- Generate Password ----------
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # ---------- Password Strength ----------
    if length < 12:
        strength = "🔴 Weak"

    elif length < 16:
        if include_numbers or include_symbols:
            strength = "🟡 Medium"
        else:
            strength = "🔴 Weak"

    else:
        if include_numbers and include_symbols:
            strength = "🟢 Strong"
        elif include_numbers or include_symbols:
            strength = "🟡 Medium"
        else:
            strength = "🟡 Medium"

    # ---------- Output ----------
    print("\n" + "=" * 40)
    print("      PASSWORD GENERATED")
    print("=" * 40)
    print("Password :", password)
    print("Strength :", strength)
    print("=" * 40)

    # ---------- Generate Again ----------
    while True:
        again = input("\nGenerate another password? (Y/N): ").strip().lower()

        if again in ["y", "yes"]:
            print()
            break

        elif again in ["n", "no"]:
            print("\nThank you for using Password Generator!")
            exit()

        else:
            print("❌ Invalid option! Please type Y, N, Yes, or No.")