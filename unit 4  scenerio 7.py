
mport numpy as np
import pandas as pd

# Create NumPy array of treatment costs
costs = np.array([15000, 25000, 18000, 30000, 22000])

# Calculate mean, maximum and minimum
print("Mean Treatment Cost:", np.mean(costs))
print("Maximum Treatment Cost:", np.max(costs))
print("Minimum Treatment Cost:", np.min(costs))

# Create Pandas DataFrame
data = {
    'Patient Name': ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohit'],
    'Treatment Cost': costs
}

df = pd.DataFrame(data)

# Display patient details
print("\nPatient Details:")
print(df)

# Display patients whose cost exceeds ₹20,000
print("\nPatients with Treatment Cost Above ₹20,000:")
print(df[df['Treatment Cost'] > 20000])