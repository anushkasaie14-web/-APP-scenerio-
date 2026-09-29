import csv
import argparse

# Accept filename using argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

# Read mobile records from CSV file
with open(args.filename, "r") as file:
    reader = csv.DictReader(file)

    mobiles = list(reader)

# Display all mobile records
print("All Mobile Records:")
for mobile in mobiles:
    print(mobile)

# Search mobile using Brand Name
brand = input("\nEnter Brand Name to search: ")

print("\nSearch Result:")
found = False

for mobile in mobiles:
    if mobile["Brand"].lower() == brand.lower():
        print(mobile)
        found = True

if not found:
    print("Mobile not found")