import pandas as pd
import glob
import os

# Folder containing the CSV files
data_folder = "data/"

# Get all CSV files (this will find all three, regardless of names)
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

# List to hold processed dataframes
all_data = []

for file in csv_files:
    print(f"Processing: {file}")
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'pink morsel']
    
    # Calculate sales = quantity * price
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only required columns: sales, date, region
    df = df[['sales', 'date', 'region']]
    
    all_data.append(df)

# Combine all data
final_df = pd.concat(all_data, ignore_index=True)

# Save to a new CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Processing complete. Output saved to formatted_data.csv")