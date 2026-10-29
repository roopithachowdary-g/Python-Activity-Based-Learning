
# Comprehensive Smart Campus Management Simulation

students = []
attendance = []
marks = []
registrations = []
resources = [
    ("Projector", 2),
    ("Computer", 5),
    ("Sports Kit", 3)
]

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Student Records")
    print("2. Attendance Management")
    print("3. Marks Management")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Student records
    if choice == "1":
        roll = input("Enter roll number: ")

        if any(s[0] == roll for s in students):
            print("Student already exists.")
        else:
            name = input("Enter student name: ")
            course = input("Enter course: ")

            # Tuple stores student details
            student = (roll, name, course)
            students.append(student)
            print("Student record added successfully.")

        print("\nStudent Records:")
        for roll, name, course in students:
            print(roll, name, course)

    # 2. Attendance management
    elif choice == "2":
        roll = input("Enter student roll number: ")

        if not any(s[0] == roll for s in students):
            print("Student not found.")
        else:
            status = input("Present or Absent (P/A): ").upper()

            if status in ("P", "A"):
                # Nested list: [roll, present, total]
                record = next(
                    (a for a in attendance if a[0] == roll),
                    None
                )

                if record is None:
                    attendance.append([
                        roll, 1 if status == "P" else 0, 1
                    ])
                else:
                    record[1] += 1 if status == "P" else 0
                    record[2] += 1

                print("Attendance recorded.")
            else:
                print("Invalid attendance status.")

    # 3. Marks management
    elif choice == "3":
        roll = input("Enter student roll number: ")

        if not any(s[0] == roll for s in students):
            print("Student not found.")
        else:
            scores = []
            for i in range(3):
                score = float(input(
                    f"Enter marks for subject {i + 1} (0-100): "
                ))

                while score < 0 or score > 100:
                    print("Marks must be between 0 and 100.")
                    score = float(input("Enter marks again: "))

                scores.append(score)

            record = next(
                (m for m in marks if m[0] == roll), None
            )

            if record:
                record[1] = scores
            else:
                marks.append([roll, scores])

            print("Total marks:", sum(scores))
            print("Average marks:", round(sum(scores) / 3, 2))

    # 4. Event registration
    elif choice == "4":
        roll = input("Enter student roll number: ")

        if not any(s[0] == roll for s in students):
            print("Student not found.")
        else:
            event = input("Enter event name: ").strip()

            if not event:
                print("Event name cannot be empty.")
            elif (event.lower(), roll) in [
                (e.lower(), r) for e, r in registrations
            ]:
                print("Already registered for this event.")
            else:
                registrations.append((event, roll))
                print("Event registration successful.")

    # 5. Resource allocation
    elif choice == "5":
        print("\nAvailable Resources:")
        for resource, quantity in resources:
            print(resource, "- Available:", quantity)

        resource_name = input("Enter resource name: ").strip()
        quantity = int(input("Enter quantity to allocate: "))

        for i, (resource, available) in enumerate(resources):
            if resource.lower() == resource_name.lower():
                if quantity > 0 and quantity <= available:
                    resources[i] = (resource, available - quantity)
                    print("Resource allocated successfully.")
                else:
                    print("Invalid quantity or insufficient stock.")
                break
        else:
            print("Resource not found.")

    # 6. Summary report
    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")
        print("Total students:", len(students))
        print("Attendance records:", len(attendance))
        print("Students with marks:", len(marks))
        print("Event registrations:", len(registrations))

        print("\nStudent Performance:")
        for roll, scores in marks:
            print(roll, "Total:", sum(scores),
                  "Average:", round(sum(scores) / len(scores), 2))

        print("\nAttendance Percentages:")
        for roll, present, total in attendance:
            percentage = present / total * 100
            print(roll, round(percentage, 2), "%")

        print("\nEvent Registrations:")
        for event, roll in registrations:
            print(event, "-", roll)

        print("\nRemaining Resources:")
        for resource, quantity in resources:
            print(resource, "-", quantity)

    # 7. Exit
    elif choice == "7":
        print("Thank you for using Smart Campus Management.")
        break

    else:
        print("Invalid choice. Please select 1 to 7.")

