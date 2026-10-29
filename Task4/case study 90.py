
# Integrated Campus Energy and Water Audit

buildings = int(input("Enter number of buildings: "))
days = int(input("Enter number of days: "))

if buildings <= 0 or days <= 0:
    print("Buildings and days must be positive.")
else:
    electricity_rate = float(input("Electricity cost per unit: Rs. "))
    water_rate = float(input("Water cost per unit: Rs. "))

    energy_limit = float(input("Daily electricity limit per building: "))
    water_limit = float(input("Daily water limit per building: "))

    records = []

    # Input daily consumption
    for i in range(buildings):
        name = input(f"\nEnter building {i + 1} name: ")
        energy = []
        water = []

        for d in range(days):
            print(f"Day {d + 1} - {name}")
            e = float(input("Electricity units: "))
            w = float(input("Water units: "))

            if e < 0 or w < 0:
                print("Consumption cannot be negative.")
                e = 0
                w = 0

            energy.append(e)
            water.append(w)

        records.append({
            "name": name,
            "energy": energy,
            "water": water
        })

    # Calculate totals and percentage changes
    for b in records:
        b["total_energy"] = sum(b["energy"])
        b["total_water"] = sum(b["water"])

        b["energy_cost"] = b["total_energy"] * electricity_rate
        b["water_cost"] = b["total_water"] * water_rate

        first_e = b["energy"][0]
        last_e = b["energy"][-1]
        first_w = b["water"][0]
        last_w = b["water"][-1]

        b["energy_change"] = (
            (last_e - first_e) / first_e * 100
            if first_e != 0 else None
        )

        b["water_change"] = (
            (last_w - first_w) / first_w * 100
            if first_w != 0 else None
        )

        b["excess"] = (
            any(x > energy_limit for x in b["energy"])
            or any(x > water_limit for x in b["water"])
        )

    # Calculate scores using maximum building totals
    max_energy = max(b["total_energy"] for b in records)
    max_water = max(b["total_water"] for b in records)

    for b in records:
        energy_score = (
            b["total_energy"] / max_energy * 100
            if max_energy > 0 else 0
        )
        water_score = (
            b["total_water"] / max_water * 100
            if max_water > 0 else 0
        )

        b["score"] = 0.6 * energy_score + 0.4 * water_score

    # Rank buildings from highest score
    ranked = sorted(
        records, key=lambda b: b["score"], reverse=True
    )

    # Display audit report
    print("\n--- CAMPUS ENERGY AND WATER AUDIT ---")

    for b in ranked:
        print("\nBuilding:", b["name"])
        print("Electricity:", b["total_energy"], "units")
        print("Water:", b["total_water"], "units")
        print("Electricity cost: Rs.", round(b["energy_cost"], 2))
        print("Water cost: Rs.", round(b["water_cost"], 2))
        print("Total cost: Rs.",
              round(b["energy_cost"] + b["water_cost"], 2))

        print("Electricity change:",
              "Undefined" if b["energy_change"] is None
              else str(round(b["energy_change"], 2)) + "%")

        print("Water change:",
              "Undefined" if b["water_change"] is None
              else str(round(b["water_change"], 2)) + "%")

        print("Consumption status:",
              "Excessive" if b["excess"] else "Within limits")
        print("Score:", round(b["score"], 2))

    print("\n--- BUILDING RANKING ---")
    for rank, b in enumerate(ranked, start=1):
        print(rank, b["name"], "- Score:", round(b["score"], 2))

