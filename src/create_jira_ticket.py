import csv
import os

THRESHOLD_PERCENT = 30

os.makedirs("jira_tickets", exist_ok=True)

with open("sample-data/variance_events.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        variance = float(row["variance_percent"])

        if variance >= THRESHOLD_PERCENT:

            filename = f"jira_tickets/{row['account_name']}_ticket.txt"

            with open(filename, "w") as ticket:

                ticket.write(f"""
JIRA TICKET
========================

Summary:
{row['service']} spend increased {variance}% in account {row['account_name']}

Owner:
{row['owner_email']}

Cost Context:
Previous Cost: ${row['previous_month_cost']}
Current Cost: ${row['current_month_cost']}

Recommended Investigation:
Review workload activity, deployments, configuration changes, or demand shifts.

Requested Action:
Provide root-cause explanation and remediation plan within SLA.
""")

            print(f"Ticket created: {filename}")
