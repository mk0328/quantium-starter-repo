import pandas as pd
import glob
import os

data_folder = "data/"
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

all_data = []

for file in csv_files:
    print(f"Processing: {file}")
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'pink morsel']
    
    # Clean the price column: remove '$' and convert to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Calculate sales = quantity * price
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only required columns: sales, date, region
    df = df[['sales', 'date', 'region']]
    
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv('formatted_data.csv', index=False)

print("Processing complete. Output saved to formatted_data.csv")