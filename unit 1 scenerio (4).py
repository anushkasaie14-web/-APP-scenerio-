class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Category:", self.category())
        print("-------------------")


# Creating mobile objects
m1 = Mobile("Apple", "iPhone 15", 65000)
m2 = Mobile("Samsung", "Galaxy A55", 35000)
m3 = Mobile("Redmi", "Note 13", 15000)

# Display details
m1.display()
m2.display()
m3.display()