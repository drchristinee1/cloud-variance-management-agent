import csv

THRESHOLD_PERCENT = 30

with open("sample-data/variance_events.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        variance = float(row["variance_percent"])

        if variance >= THRESHOLD_PERCENT:
            print("Variance Detected")
            print("-----------------")
            print(f"Account: {row['account_name']}")
            print(f"Service: {row['service']}")
            print(f"Variance: {variance}%")
            print(f"Owner: {row['owner_email']}")
            print()
