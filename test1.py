import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("test1.csv")

# Show the data
print("Data from CSV:")
print(data)

# Plot the data (bar chart)
plt.bar(data["Name"], data["Sales"], color="skyblue")
plt.title("Sales by Person")
plt.xlabel("Name")
plt.ylabel("Sales")
plt.show()
