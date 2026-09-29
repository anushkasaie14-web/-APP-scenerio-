class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for p in self.products:
            print("Product ID:", p.product_id)
            print("Product Name:", p.name)
            print("Price:", p.price)
            print("Category:", p.category())
            print("--------------------")


# Create Inventory
inventory = Inventory()

# Add Products
inventory.add_product(Product(101, "Keyboard", 1200))
inventory.add_product(Product(102, "Mouse", 500))
inventory.add_product(Product(103, "Headphones", 2000))

# Display all products
inventory.display_products()