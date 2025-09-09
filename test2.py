import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Main function to read data and create visualizations.
    """
    file_path = "test2.csv"

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # --- Visualization 1: Scatter plot of Mileage vs. Price ---
        print("Creating scatter plot for Mileage vs. Price...")
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Mileage'], df['Price'], alpha=0.6, color='blue')
        plt.title('Car Price vs. Mileage', fontsize=16)
        plt.xlabel('Mileage', fontsize=12)
        plt.ylabel('Price', fontsize=12)
        plt.grid(True)
        plt.show()

        # --- Visualization 2: Bar chart of Average Price by Fuel Type ---
        print("Creating bar chart for Average Price by Fuel Type...")
        # Group the data by 'Fuel type' and calculate the mean price for each group
        avg_price_by_fuel = df.groupby('Fuel type')['Price'].mean().reset_index()

        plt.figure(figsize=(10, 6))
        plt.bar(avg_price_by_fuel['Fuel type'], avg_price_by_fuel['Price'], color=['orange', 'green', 'purple'])
        plt.title('Average Car Price by Fuel Type', fontsize=16)
        plt.xlabel('Fuel Type', fontsize=12)
        plt.ylabel('Average Price', fontsize=12)
        plt.grid(axis='y', linestyle='--')
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure the file is in the same directory as the script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
