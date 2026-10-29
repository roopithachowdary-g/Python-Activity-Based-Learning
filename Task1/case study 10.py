
import math

# Input event expenses
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost: "))

# Input financial details
participants = int(input("Enter expected participants: "))
fee = float(input("Enter contribution per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate total cost
total_cost = venue + equipment + catering + transport + certificate

# Calculate participant contributions
contributions = participants * fee

# Calculate total available funds
total_funds = contributions + sponsorship

# Calculate funding shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate minimum registrations to break even
if fee > 0:
    minimum = math.ceil(max(0, total_cost - sponsorship) / fee)
    print("Minimum registrations needed:", minimum)
else:
    print("Minimum registrations cannot be calculated with zero contribution.")

# Display results
print("Total event cost: Rs.", total_cost)
print("Participant contributions: Rs.", contributions)
print("Total available funds: Rs.", total_funds)
print("Sponsorship/funding shortfall: Rs.", shortfall)

if total_funds >= total_cost:
    print("The event budget is covered.")
else:
    print("Additional funds are required.")

