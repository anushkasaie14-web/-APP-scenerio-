class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Category:", self.category())
        print("------------------------")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all(self):
        print("===== PRODUCT INVENTORY =====")
        for product in self.products:
            product.display()


# Creating products
p1 = Product(101, "iPhone 15", 70000)
p2 = Product(102, "Samsung Galaxy", 45000)
p3 = Product(103, "Redmi Note", 15000)

# Creating inventory
inventory = Inventory()

# Adding products
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Display all products
inventory.display_all()