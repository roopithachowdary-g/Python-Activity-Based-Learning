
# Student Timetable Conflict Detection

courses = []
unavailable_rooms = []

n = int(input("Enter number of courses: "))

# Input course schedules
for i in range(n):
    print("\nCourse", i + 1)

    name = input("Enter course name: ")
    day = input("Enter day: ").lower()
    start = int(input("Enter start hour (0-23): "))
    end = int(input("Enter end hour (1-24): "))
    room = input("Enter room number: ")

    if not (0 <= start < end <= 24):
        print("Invalid time. Enter this course again.")
        continue

    # Store schedule as a tuple
    courses.append((name, day, start, end, room))

# Input unavailable room schedules
m = int(input("\nEnter number of unavailable room periods: "))

for i in range(m):
    print("\nUnavailable period", i + 1)

    room = input("Enter room number: ")
    day = input("Enter day: ").lower()
    start = int(input("Enter start hour: "))
    end = int(input("Enter end hour: "))

    unavailable_rooms.append((room, day, start, end))

conflicts = []

# Compare course schedules
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        # Check overlapping class times
        if (c1[1] == c2[1] and
            c1[2] < c2[3] and c2[2] < c1[3]):

            conflicts.append(
                f"Time conflict: {c1[0]} and {c2[0]}"
            )

# Check room availability
for course in courses:
    for room in unavailable_rooms:
        if (course[4] == room[0] and
            course[1] == room[1] and
            course[2] < room[3] and
            room[2] < course[3]):

            conflicts.append(
                f"Room conflict: {course[0]} in room {course[4]}"
            )

# Display results
print("\n--- TIMETABLE VALIDATION ---")

if conflicts:
    for conflict in conflicts:
        print(conflict)

    print("Timetable is INVALID.")
else:
    print("No conflicts found.")
    print("Timetable is VALID.")

