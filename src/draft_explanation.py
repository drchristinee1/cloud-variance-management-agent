import csv

THRESHOLD_PERCENT = 30

with open("sample-data/variance_events.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        variance = float(row["variance_percent"])

        if variance >= THRESHOLD_PERCENT:

            explanation = f"""
JIRA DRAFT
--------------------------------
Summary:
{row['service']} spend increased {variance}% in account {row['account_name']}.

Owner:
{row['owner_email']}

Context:
Previous cost: ${row['previous_month_cost']}
Current cost: ${row['current_month_cost']}

Recommended Investigation:
Please review workload activity, deployment changes, configuration updates, or demand changes contributing to this increase.

Requested Action:
Provide root-cause explanation and remediation plan within SLA window.
"""

            print(explanation)
