
import re

# Student Email and Identifier Validation

email = input("Enter student email: ").strip()
reg_id = input("Enter registration ID: ").strip()

email_errors = []
id_errors = []

# Email validation
if email.count("@") == 0:
    email_errors.append("Missing @ symbol.")
elif email.count("@") > 1:
    email_errors.append("Multiple @ symbols found.")

if email.count("@") == 1:
    username, domain = email.split("@")

    if not username:
        email_errors.append("Missing username.")

    if not domain:
        email_errors.append("Missing domain.")

    if username and not re.fullmatch(
        r"[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*", username
    ):
        email_errors.append(
            "Invalid username characters or separators."
        )

    if domain and not re.fullmatch(
        r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*"
        r"\.[A-Za-z]{2,}", domain
    ):
        email_errors.append(
            "Invalid domain or missing domain extension."
        )

# Registration ID validation
# Required format: CSE-2026-001
parts = reg_id.split("-")

if len(parts) != 3:
    id_errors.append(
        "Incorrect separators or missing components."
    )
else:
    prefix, year, number = parts

    if not prefix:
        id_errors.append("Missing department prefix.")
    elif not re.fullmatch(r"[A-Z]{2,5}", prefix):
        id_errors.append(
            "Prefix must contain 2-5 uppercase letters."
        )

    if not year:
        id_errors.append("Missing year.")
    elif not re.fullmatch(r"\d{4}", year):
        id_errors.append("Year must contain 4 digits.")

    if not number:
        id_errors.append("Missing student number.")
    elif not re.fullmatch(r"\d{3}", number):
        id_errors.append(
            "Student number must contain 3 digits."
        )

# Display email result
print("\n--- EMAIL VALIDATION ---")
if email_errors:
    for error in email_errors:
        print("Error:", error)
    print("Email: INVALID")
else:
    print("Email: VALID")

# Display registration ID result
print("\n--- REGISTRATION ID VALIDATION ---")
if id_errors:
    for error in id_errors:
        print("Error:", error)
    print("Registration ID: INVALID")
else:
    print("Registration ID: VALID")

