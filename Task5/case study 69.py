
import statistics

# Nested List Sports Performance Analysis

players = []
n = int(input("Enter number of players: "))
m = int(input("Enter number of matches: "))

if n <= 0 or m <= 0:
    print("Players and matches must be greater than zero.")

else:
    # Input player scores
    for i in range(n):
        name = input("\nEnter player name: ")
        scores = []

        for j in range(m):
            score = float(input(
                f"Enter score for match {j + 1}: "
            ))
            scores.append(score)

        players.append([name, scores])

    # Calculate performance statistics
    results = []

    for player in players:
        name = player[0]
        scores = player[1]

        total = sum(scores)
        average = total / m

        if m > 1:
            consistency = statistics.pstdev(scores)
        else:
            consistency = 0

        change = scores[-1] - scores[0]

        if change > 0:
            trend = "Improving"
        elif change < 0:
            trend = "Declining"
        else:
            trend = "Stable"

        results.append([
            name, total, average, consistency, trend
        ])

    # Ranking rules:
    # 1. Higher average score
    # 2. Lower standard deviation
    # 3. Higher total score
    results.sort(
        key=lambda x: (-x[2], x[3], -x[1])
    )

    # Display results
    print("\n--- SPORTS PERFORMANCE REPORT ---")

    for rank, player in enumerate(results, start=1):
        print("\nRank:", rank)
        print("Player:", player[0])
        print("Total score:", player[1])
        print("Average score:", round(player[2], 2))
        print("Standard deviation:",
              round(player[3], 2))
        print("Performance trend:", player[4])

