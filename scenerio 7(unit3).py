import csv
import re

# Read customer records
with open("customers.csv", "r") as file:
    reader = csv.DictReader(file)
    customers = list(reader)

# Display all customer details
print("All Customer Records:")
for customer in customers:
    print(customer)

# Search using Account Number
account = input("\nEnter Account Number: ")

# Validate account number using Regular Expression
if not re.fullmatch(r"\d{10}", account):
    print("Invalid Account Number")
else:
    found = False

    for customer in customers:
        if customer["Account Number"] == account:
            print("\nCustomer Found:")
            print(customer)
            found = True
            break

    if not found:
        print("Customer not found")