# Mobile Store Management System

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = int(price)

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"


premium = 0
midrange = 0
budget = 0

# Read data from file
with open("mobiles.txt", "r") as file:
    for line in file:
        brand, model, price = line.strip().split(",")
        mobile = Mobile(brand, model, price)

        print(mobile.brand, mobile.model, mobile.price, mobile.category())

        if mobile.category() == "Premium":
            premium += 1
        elif mobile.category() == "Mid-range":
            midrange += 1
        else:
            budget += 1

print("\nCount:")
print("Premium:", premium)
print("Mid-range:", midrange)
print("Budget:", budget)