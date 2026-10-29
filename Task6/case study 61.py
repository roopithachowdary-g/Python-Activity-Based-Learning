
# Nested List Examination Seating Validation

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input valid student roll numbers
valid_rolls = input(
    "Enter valid roll numbers separated by spaces: "
).split()

# Input seating matrix
seating = []

print("\nEnter roll numbers for each seat (0 = empty):")

for i in range(rows):
    row = []
    for j in range(cols):
        roll = input(
            f"Seat [{i + 1},{j + 1}]: "
        ).strip()
        row.append(roll)
    seating.append(row)

# Input reserved seat positions (1-based)
reserved_count = int(input("Enter number of reserved seats: "))
reserved = set()

for i in range(reserved_count):
    r = int(input("Reserved seat row: "))
    c = int(input("Reserved seat column: "))
    reserved.add((r - 1, c - 1))

errors = []
roll_positions = {}

# Validate every seat
for i in range(rows):
    for j in range(cols):
        roll = seating[i][j]
        position = (i, j)

        if position in reserved:
            if roll != "0":
                errors.append(
                    f"Reserved seat [{i+1},{j+1}] is occupied."
                )
            continue

        if roll == "0":
            errors.append(
                f"Empty seat at [{i+1},{j+1}]."
            )
            continue

        if roll not in valid_rolls:
            errors.append(
                f"Invalid roll number {roll} "
                f"at [{i+1},{j+1}]."
            )

        roll_positions.setdefault(roll, []).append(
            (i + 1, j + 1)
        )

# Check duplicate roll numbers
for roll, positions in roll_positions.items():
    if len(positions) > 1:
        errors.append(
            f"Duplicate roll number {roll} at {positions}."
        )

# Display seating matrix
print("\n--- SEATING MATRIX ---")
for row in seating:
    print(row)

# Display validation report
print("\n--- VALIDATION REPORT ---")

if errors:
    for error in errors:
        print(error)

    print("\nSeating Arrangement: INVALID")
else:
    print("No errors found.")
    print("Seating Arrangement: VALID")

