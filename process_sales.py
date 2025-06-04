import pandas as pd
import glob


data_folder = './data/'


csv_files = glob.glob(data_folder + '*.csv')

# List to hold processed dataframes
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    # Filter only Pink Morsel rows
    df = df[df['product'] == 'Pink Morsel']
    # Calculate Sales
    df['Sales'] = df['quantity'] * df['price']
    # Select only Sales, Date, Region columns
    df = df[['Sales', 'date', 'region']]
    dfs.append(df)

# Combine all dataframes into one
final_df = pd.concat(dfs, ignore_index=True)


final_df.to_csv('processed_sales.csv', index=False)

print("Processed data saved to 'processed_sales.csv'")
