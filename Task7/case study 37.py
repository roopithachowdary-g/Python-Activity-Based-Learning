
# Nested Loop Calendar Generator

month = input("Enter month name: ")
weekday = input("Enter starting weekday: ").strip().capitalize()
days = int(input("Enter number of days in the month: "))

weekdays = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

if weekday not in weekdays:
    print("Invalid starting weekday.")

elif days not in [28, 29, 30, 31]:
    print("Invalid number of days.")

else:
    start = weekdays.index(weekday)

    print("\n       ", month)
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Nested loops generate calendar rows and columns
    day = 1

    for week in range(6):
        for column in range(7):

            position = week * 7 + column

            if position < start:
                print("    ", end="")

            elif day <= days:
                print(f"{day:3} ", end="")
                day += 1

            else:
                print("    ", end="")

        print()

        if day > days:
            break

