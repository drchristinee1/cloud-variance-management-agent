import csv

THRESHOLD_PERCENT = 30

def infer_likely_driver(service, variance):
    if service == "AWSLambda" and variance >= 100:
        return "Possible runaway execution, recursive invocation, or sudden traffic increase."
    elif service == "AmazonEC2":
        return "Possible instance scale-up, new workload deployment, or underutilized compute."
    elif service == "AmazonRDS":
        return "Possible database growth, storage increase, higher I/O, or instance size change."
    else:
        return "Requires workload and configuration review."

def assign_priority(variance):
    if variance >= 100:
        return "P1 - Critical"
    elif variance >= 50:
        return "P2 - High"
    elif variance >= 30:
        return "P3 - Medium"
    else:
        return "Monitor"

with open("sample-data/variance_events.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        variance = float(row["variance_percent"])

        if variance >= THRESHOLD_PERCENT:
            likely_driver = infer_likely_driver(row["service"], variance)
            priority = assign_priority(variance)

            print("AI REASONING SUMMARY")
            print("====================")
            print(f"Account: {row['account_name']}")
            print(f"Service: {row['service']}")
            print(f"Variance: {variance}%")
            print(f"Likely Driver: {likely_driver}")
            print(f"Priority: {priority}")
            print(f"Recommended Action: Open Jira ticket and request owner response within SLA.")
            print()
