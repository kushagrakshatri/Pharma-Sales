#anomaly_detection.py

import pandas as pd
import os
from sklearn.ensemble import IsolationForest

def detect_anomalies(file_path):
    # Read the cleaned CSV file
    df = pd.read_csv(file_path)
    
    # Assuming 'total_sales' is the column to check for anomalies
    if 'total_sales' in df.columns:
        # Initialize the Isolation Forest model
        model = IsolationForest(contamination=0.05)
        
        # Fit the model
        df['anomaly'] = model.fit_predict(df[['total_sales']])
        
        # Filter anomalies
        anomalies = df[df['anomaly'] == -1]
        
        # Save anomalies to a new CSV file
        anomaly_file_path = file_path.replace('_cleaned.csv', '_anomalies.csv')
        anomalies.to_csv(anomaly_file_path, index=False)
        print(f"Anomalies detected and saved to {anomaly_file_path}")

def main():
    # Directory containing the cleaned CSV files
    csv_dir = 'csv'
    
    # Process each cleaned CSV file in the directory
    for file_name in os.listdir(csv_dir):
        if file_name.endswith('_cleaned.csv'):
            file_path = os.path.join(csv_dir, file_name)
            detect_anomalies(file_path)

if __name__ == "__main__":
    main()
