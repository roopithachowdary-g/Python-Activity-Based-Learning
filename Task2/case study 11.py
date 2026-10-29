
import math

# Input examination rules
n = int(input("Enter number of subjects: "))
maximum = float(input("Enter maximum marks per subject: "))
pass_mark = float(input("Enter minimum pass marks: "))
grace_limit = float(input("Enter grace mark limit per subject: "))

if n <= 0 or maximum <= 0 or not (0 <= pass_mark <= maximum) or grace_limit < 0:
    print("Invalid examination rules.")
else:
    total = 0
    failed = False

    for i in range(1, n + 1):
        marks = float(input(f"Enter marks for subject {i}: "))

        if marks < 0 or marks > maximum:
            print("Invalid marks. Enter marks again.")
            marks = float(input(f"Enter valid marks for subject {i}: "))

            while marks < 0 or marks > maximum:
                print("Marks must be between 0 and", maximum)
                marks = float(input(f"Enter valid marks for subject {i}: "))

        grace = 0

        if marks < pass_mark:
            needed = pass_mark - marks

            if needed <= grace_limit:
                grace = min(needed, maximum - marks)
                marks += grace

        if marks >= pass_mark:
            result = "Pass"
        else:
            result = "Fail"
            failed = True

        total += marks

        print("Subject", i)
        print("Final marks:", marks)
        print("Grace marks applied:", grace)
        print("Result:", result)

    percentage = (total / (n * maximum)) * 100

    if failed:
        classification = "Fail"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass"

    print("\n--- FINAL EXAMINATION RESULT ---")
    print("Total marks:", total, "/", n * maximum)
    print("Percentage:", round(percentage, 2), "%")
    print("Final classification:", classification)

