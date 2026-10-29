# Problem Statement
The Campus Event Financial Planning program is used to calculate the total expenses required to organize a college event. It considers venue, equipment, catering, transport, and certificate costs. The program also calculates the contribution required from each participant, the sponsorship shortfall, and the minimum number of registrations needed to break even. This helps the event organizers plan their budget and manage expenses effectively.
# Algorithm
1. Start the program.
2. Input the venue cost, equipment cost, catering cost, transport cost, and certificate cost.
3. Input the expected number of participants, contribution per participant, and sponsorship amount.
4. Calculate the total event cost by adding all five expenses.
5. Calculate the total participant contribution by multiplying the number of participants by the contribution per participant.
6. Calculate the total available funds by adding participant contributions and sponsorship.
7. Calculate the sponsorship shortfall if the available funds are less than the total event cost.
8. Calculate the minimum registration count required to break even using the funds needed after sponsorship.
9. Display the total cost, participant contributions, sponsorship shortfall, and minimum registration count.
10. Stop the program.
# Mermaid Flowchart
```mermaid
  flowchart TD
    A([Start]) --> B[/Input venue, equipment, catering, transport and certificate costs/]
    B --> C[/Input participants, fee per participant and sponsorship/]
    C --> D[Calculate total event cost]
    D --> E[Calculate participant contributions]
    E --> F[Calculate total available funds]
    F --> G[Calculate sponsorship shortfall]
    G --> H[Calculate minimum registrations to break even]
    H --> I[/Display all financial results/]
    I --> J([Stop])
  ```
  # Sample input
  Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 20000
Enter transport cost: 5000
Enter certificate cost: 2000
Enter expected participants: 100
Enter contribution per participant: 300
Enter sponsorship amount: 10000
