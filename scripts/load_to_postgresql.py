#load_to_postgresql.py

import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

def load_to_postgresql(file_path, table_name, db_url):
    # Read the cleaned CSV file
    df = pd.read_csv(file_path)
    
    # Create a connection to the PostgreSQL database
    engine = create_engine(db_url)
    
    # Load data into the specified table
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data from {file_path} loaded into table {table_name}")

def main():
    # Database connection URL
    db_url = 'postgresql://username:password@localhost:5432/mydatabase'
    
    # Directory containing the cleaned CSV files
    csv_dir = 'csv'
    
    # Process each cleaned CSV file in the directory
    for file_name in os.listdir(csv_dir):
        if file_name.endswith('_cleaned.csv'):
            file_path = os.path.join(csv_dir, file_name)
            table_name = file_name.replace('_cleaned.csv', '')
            load_to_postgresql(file_path, table_name, db_url)

if __name__ == "__main__":
    main()
