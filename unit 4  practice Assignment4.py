import numpy as np
import pandas as pd

# Create NumPy array of book prices
prices = np.array([250, 450, 600, 750, 900])

# Calculate average book price
average = np.mean(prices)
print("Average Book Price: ₹", average)

# Create Pandas DataFrame
data = {
    'Book Name': ['Python', 'Java', 'DBMS', 'DSA', 'AI'],
    'Price': prices
}

df = pd.DataFrame(data)

# Display all books
print("\nBook Details:")
print(df)

# Display books costing more than ₹500
print("\nBooks costing more than ₹500:")
print(df[df['Price'] > 500])