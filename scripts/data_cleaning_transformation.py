#data_cleaning_transformation.py

import pandas as pd
import os

def clean_and_transform(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Example cleaning operations
    # Remove rows with missing values
    df.dropna(inplace=True)
    
    # Convert date column to datetime format if exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    
    # Example transformation operations
    # Add a new column for total sales if applicable
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total_sales'] = df['quantity'] * df['price']
    
    # Save the cleaned and transformed data
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned and transformed data saved to {cleaned_file_path}")

def main():
    # Directory containing the CSV files
    csv_dir = 'csv'
    
    # Process each CSV file in the directory
    for file_name in os.listdir(csv_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(csv_dir, file_name)
            clean_and_transform(file_path)

if __name__ == "__main__":
    main()
